#!/usr/bin/env python3
"""Update GitHub profile README with latest stats from GitHub API.

IMPORTANT: This script runs publicly via GitHub Actions.
It MUST filter out private repositories and never expose their names,
descriptions, or any identifying details. Only aggregate counts and
language breakdowns are allowed for private repos.
"""
import base64
import json
import os
import re
import urllib.request
from collections import Counter
from datetime import datetime, timezone

TOKEN = os.environ.get("GH_TOKEN", os.environ.get("GITHUB_TOKEN", ""))
USERNAME = "GuilhermeP96"
API = "https://api.github.com"
GRAPHQL = "https://api.github.com/graphql"


def github_graphql(query):
    data = json.dumps({"query": query}).encode("utf-8")
    req = urllib.request.Request(
        GRAPHQL,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "profile-updater",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def github_rest(path):
    url = f"{API}{path}" if path.startswith("/") else path
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "profile-updater",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def fetch_profile():
    query = """
    {
      user(login: "%s") {
        followers { totalCount }
        following { totalCount }
        repositories(first: 100, ownerAffiliations: [OWNER, COLLABORATOR]) {
          totalCount
          nodes {
            name
            isPrivate
            isFork
            stargazerCount
            forkCount
            url
            primaryLanguage { name }
            parent { nameWithOwner }
          }
        }
        pullRequests(first: 20, orderBy: {field: CREATED_AT, direction: DESC}) {
          totalCount
          nodes {
            title
            state
            url
            repository { nameWithOwner isPrivate }
            createdAt
            mergedAt
          }
        }
      }
    }
    """ % USERNAME
    return github_graphql(query)["data"]["user"]


def fetch_fork_branches(fork_name):
    """Fetch non-default branches from a forked repo."""
    try:
        branches = github_rest(f"/repos/{USERNAME}/{fork_name}/branches")
        repo = github_rest(f"/repos/{USERNAME}/{fork_name}")
        default = repo.get("default_branch", "main")
        return [b["name"] for b in branches if b["name"] != default]
    except Exception:
        return []


def fetch_pyaccelerate_stats():
    try:
        repo = github_rest(f"/repos/{USERNAME}/pyaccelerate")
    except Exception:
        return None

    modules = 0
    try:
        contents = github_rest(
            f"/repos/{USERNAME}/pyaccelerate/contents/src/pyaccelerate"
        )
        modules = len(
            [
                c
                for c in contents
                if c["name"].endswith(".py") and not c["name"].startswith("_")
            ]
        )
        # count subdirectories as additional modules
        modules += len([c for c in contents if c["type"] == "dir" and not c["name"].startswith("_")])
    except Exception:
        pass

    test_files = 0
    try:
        tests = github_rest(f"/repos/{USERNAME}/pyaccelerate/contents/tests")
        test_files = len([c for c in tests if c["name"].startswith("test_")])
    except Exception:
        pass

    version = "?"
    try:
        releases = github_rest(f"/repos/{USERNAME}/pyaccelerate/releases")
        if releases:
            version = releases[0].get("tag_name", "?").lstrip("v")
    except Exception:
        pass

    return {
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "version": version,
        "modules": modules,
        "test_files": test_files,
    }


def build_prs_table(prs):
    """Build PR table using ONLY PRs on public repositories."""
    rows = []
    for pr in prs:
        # Skip PRs on private repos
        repo_info = pr.get("repository", {})
        if repo_info.get("isPrivate", False):
            continue
        state = pr["state"]
        if state == "MERGED":
            badge = "![Merged](https://img.shields.io/badge/-Merged-8957e5)"
        elif state == "OPEN":
            badge = "![Open](https://img.shields.io/badge/-Open-238636)"
        else:
            badge = "![Closed](https://img.shields.io/badge/-Closed-da3633)"
        date = (pr["mergedAt"] or pr["createdAt"])[:10]
        repo = pr["repository"]["nameWithOwner"]
        title = pr["title"].replace("|", "\\|")
        rows.append(f"| [{title}]({pr['url']}) | {repo} | {badge} | {date} |")
    header = "| PR | Repository | Status | Date |\n|----|-----------|--------|------|"
    return header + "\n" + "\n".join(rows)


def build_forks_table(repos, prs):
    """Build forks table using ONLY public forks."""
    forks = [r for r in repos if r["isFork"] and not r["isPrivate"] and r.get("parent")]

    # map upstream repo -> latest PR
    pr_map = {}
    for pr in prs:
        rn = pr["repository"]["nameWithOwner"]
        if rn not in pr_map:
            pr_map[rn] = pr

    rows = []
    for fork in forks:
        parent = fork["parent"]["nameWithOwner"]
        pr = pr_map.get(parent)
        status = "--"
        if pr:
            if pr["state"] == "MERGED":
                status = "PR Merged"
            elif pr["state"] == "OPEN":
                status = "PR Open"
            else:
                status = "PR Closed"

        branches = fetch_fork_branches(fork["name"])
        branch_str = ", ".join(f"`{b}`" for b in branches[:3]) if branches else "--"

        rows.append(
            f"| [{fork['name']}]({fork['url']}) "
            f"| [{parent}](https://github.com/{parent}) "
            f"| {branch_str} | {status} |"
        )

    header = "| Fork | Upstream | Branch | Status |\n|------|----------|--------|--------|"
    return header + "\n" + "\n".join(rows)


def build_stats_line(profile, prs):
    repos = profile["repositories"]["nodes"]
    public_count = sum(1 for r in repos if not r["isPrivate"])
    private_count = sum(1 for r in repos if r["isPrivate"])
    followers = profile["followers"]["totalCount"]
    # Only count PRs on public repos
    public_prs = [pr for pr in prs if not pr.get("repository", {}).get("isPrivate", False)]
    total = len(public_prs)
    merged = sum(1 for pr in public_prs if pr["state"] == "MERGED")
    return f"**{public_count}** public repos | **{private_count}** private repos | **{followers}** followers | **{total}** PRs | **{merged}** merged"


def build_private_activity(repos):
    """Build anonymous private activity summary -- only language counts, no names."""
    private = [r for r in repos if r["isPrivate"]]
    count = len(private)
    lang_counter = Counter()
    for r in private:
        lang = (r.get("primaryLanguage") or {}).get("name")
        lang_counter[lang or "Other"] += 1
    rows = []
    for lang, n in lang_counter.most_common():
        rows.append(f"| {lang} | {n} |")
    table = "| Language | Projects |\n|----------|----------|\n" + "\n".join(rows)
    return (
        f"Beyond public repos, I maintain **{count}** private projects spanning:\n\n"
        f"{table}\n\n"
        "Areas include data engineering, web apps, network automation, enterprise integrations, and tooling."
    )


def build_pyaccelerate_section(stats):
    if stats is None:
        return "*(stats unavailable)*"
    return (
        "| Metric | Value |\n"
        "|--------|-------|\n"
        f"| Version | v{stats['version']} |\n"
        f"| Modules | {stats['modules']} |\n"
        f"| Test Files | {stats['test_files']} |\n"
        f"| Stars | {stats['stars']} |\n"
        "| GPU Vendors | NVIDIA, AMD, Intel, ARM |\n"
        "| Platforms | Linux, Windows, macOS, Android/Termux, IoT/SBC |"
    )


def update_section(readme, section, content):
    pattern = (
        rf"(<!-- START_SECTION:{re.escape(section)} -->\n).*?"
        rf"(\n<!-- END_SECTION:{re.escape(section)} -->)"
    )
    return re.sub(pattern, rf"\g<1>{content}\g<2>", readme, flags=re.DOTALL)


def main():
    if not TOKEN:
        print("ERROR: GH_TOKEN or GITHUB_TOKEN env var required")
        return

    readme_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md"
    )

    print("Fetching profile data...")
    profile = fetch_profile()
    repos = profile["repositories"]["nodes"]
    prs = profile["pullRequests"]["nodes"]

    print("Fetching pyaccelerate stats...")
    pyaccelerate = fetch_pyaccelerate_stats()

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    readme = update_section(readme, "prs", build_prs_table(prs))
    readme = update_section(readme, "forks", build_forks_table(repos, prs))
    readme = update_section(readme, "stats", build_stats_line(profile, prs))
    readme = update_section(readme, "pyaccelerate", build_pyaccelerate_section(pyaccelerate))
    readme = update_section(readme, "private_activity", build_private_activity(repos))

    # Update timestamp
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    readme = re.sub(
        r"\*Last updated:.*?\*",
        f"*Last updated: {now}*",
        readme,
    )

    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)

    print(f"README updated at {now}")


if __name__ == "__main__":
    main()
