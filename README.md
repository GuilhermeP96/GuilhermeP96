<div align="center">

# Guilherme Pinheiro

**Data Engineer & Automation Specialist** @ Claro S.A. | Founder @ [Datano](https://datano.com.br)

Sao Paulo, Brazil

[![GitHub followers](https://img.shields.io/github/followers/GuilhermeP96?style=social)](https://github.com/GuilhermeP96)
[![GitHub Stars](https://img.shields.io/github/stars/GuilhermeP96?style=social&affiliations=OWNER)](https://github.com/GuilhermeP96)

</div>

---

### About

Founder of **[Datano](https://datano.com.br)** -- a data engineering & data science consultancy delivering ETL/ELT pipelines, data warehouses, ML solutions, custom dashboards, and API integrations. 50+ projects delivered across Azure (Data Factory, Databricks, Synapse), AWS, Python, SQL, and Power BI.

Creator of **[pyaccelerate](https://github.com/GuilhermeP96/pyaccelerate)** -- a Python acceleration engine with multi-GPU, NPU, IoT, and Kubernetes support.

Currently working on GPU-aware optimization for [ollama](https://github.com/ollama/ollama) and contributing to the AI inference ecosystem.

### Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white" alt="Go" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/PowerShell-5391FE?style=flat&logo=powershell&logoColor=white" alt="PowerShell" />
  <img src="https://img.shields.io/badge/Shell-4EAA25?style=flat&logo=gnubash&logoColor=white" alt="Shell" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp&logoColor=white" alt="C#" />
  <img src="https://img.shields.io/badge/PHP-777BB4?style=flat&logo=php&logoColor=white" alt="PHP" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat&logo=nvidia&logoColor=white" alt="CUDA" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/MikroTik-293239?style=flat&logo=mikrotik&logoColor=white" alt="MikroTik" />
</p>

---

### Public Projects

| Project | Description | Tech |
|---------|-------------|------|
| [pyaccelerate](https://github.com/GuilhermeP96/pyaccelerate) | High-performance Python acceleration engine -- CPU, multi-GPU, NPU, IoT, K8s, auto-tuning | Python, CUDA, Cython, Rust |
| [ollama-accelerate](https://github.com/GuilhermeP96/ollama-accelerate) | Automatic hardware detection and performance optimization for Ollama | Python |
| [python-gpu-statistical-analysis](https://github.com/GuilhermeP96/python-gpu-statistical-analysis) | GPU-accelerated statistical analysis with CuPy/CUDA and NumPy fallback | Python, CUDA |
| [animus](https://github.com/GuilhermeP96/animus) | Peer-to-peer memory sync network for GitHub Copilot & Claude Code — sessions, prompts, agents, MCP knowledge | Python, FastAPI, SQLite FTS5, WebSockets |
| [bf6-optimizer](https://github.com/GuilhermeP96/bf6-optimizer) | Battlefield 6 performance & network optimization scripts for Windows | PowerShell |
| [CSVToolBox](https://github.com/GuilhermeP96/CSVToolBox) | Toolkit for processing CSV, Excel and tabular formats | Python |
| [CSVSplitter](https://github.com/GuilhermeP96/CSVSplitter) | Split large CSV files preserving charset, separator and formatting | Python |
| [Loader](https://github.com/GuilhermeP96/Loader) | CLI tool for loading CSV data into Oracle databases | Java |
| [Spooler](https://github.com/GuilhermeP96/Spooler) | Efficient Oracle Database spool execution and CSV report generation | Java |
| [adb-toolkit](https://github.com/GuilhermeP96/adb-toolkit) | Complete Android backup, recovery & transfer with GPU acceleration | Python |
| [IEPortable](https://github.com/GuilhermeP96/IEPortable) | Cross-platform legacy IE browser with Wine ActiveX for DVRs/cameras | JavaScript |
| [PyExeBuilder](https://github.com/GuilhermeP96/PyExeBuilder) | Simple compiler for Python scripts | Python |

---

### Private Activity

<!-- START_SECTION:private_activity -->
Beyond public repos, I maintain **48** private projects spanning:

| Language | Projects |
|----------|----------|
| Python | 17 |
| PowerShell | 7 |
| TypeScript | 5 |
| Shell | 4 |
| HTML | 3 |
| Java | 2 |
| Other | 2 |
| JavaScript | 2 |
| C# | 2 |
| RouterOS Script | 2 |
| PHP | 1 |
| Jupyter Notebook | 1 |

Areas include data engineering, web apps, network automation, enterprise integrations, and tooling.
<!-- END_SECTION:private_activity -->

---

### pyaccelerate

<a href="https://github.com/GuilhermeP96/pyaccelerate">
  <img src="https://github-readme-stats-eight-theta.vercel.app/api/pin/?username=GuilhermeP96&repo=pyaccelerate&theme=tokyonight" alt="pyaccelerate" />
</a>

<!-- START_SECTION:pyaccelerate -->
| Metric | Value |
|--------|-------|
| Version | v0.11.0 |
| Modules | 27 |
| Test Files | 19 |
| Stars | 0 |
| GPU Vendors | NVIDIA, AMD, Intel, ARM |
| Platforms | Linux, Windows, macOS, Android/Termux, IoT/SBC |
<!-- END_SECTION:pyaccelerate -->

---

### AI & ML Projects

#### animus

**[Animus](https://github.com/GuilhermeP96/animus)** is a peer-to-peer memory synchronization network for GitHub Copilot and Claude Code. It collects, indexes, and syncs AI interaction context across machines through a self-hosted hub:

- **Collectors**: Copilot chat, debug logs, Claude Code transcripts, `copilot-instructions.md`, `.instructions.md`, `.prompt.md`, `.agent.md`, `/memories/` notes, and MCP knowledge graph.
- **Indexer**: Full-text + semantic search (SQLite FTS5 + sentence-transformers).
- **Sync**: HTTPS/WSS peer-to-peer replication between machines and a VPS hub.
- **CLI**: `animus` entry point for status, sync, and admin operations.

Tech: Python, FastAPI, Uvicorn, WebSockets, Pydantic, SQLite FTS5, Rich, Typer, Docker, Nginx.

#### NPS Classification Engine

Enterprise feedback classification system built for telecom NPS verbatims. It runs an **auditable cascade** that separates customer feedback from operator noise and classifies each record by product, reason, sub-reason, sentiment, root cause, and recommended action.

| Layer | Technique | Role |
|-------|-----------|------|
| 0 | Separator | Extracts customer feedback vs. operator boilerplate |
| 1 | Deterministic rules | Priority regex -- fast and auditable |
| 2 | Custom ML model | TF-IDF (word + char) + ensemble (LogReg + ComplementNB) |
| 3 | Pluggable AI | Low-confidence escalation to LLM (opt-in) |
| -- | Fallback | Manual review when confidence is too low |

Key design decisions:
- Confidence measured as margin between top-2 classes: `top1 / (top1 + top2)`.
- Multi-scenario architecture: `core/` engine + `profiles/` plug-ins; the first profile is verbatim NPS, new domains add new profiles without touching core.
- Status bands: `CLASSIFICADO` (≥ 0.90), `PENDENTE` (0.40–0.90), `ANÁLISE_MANUAL` (< 0.40).

Tech: Python, scikit-learn, pandas, regex-based rules, pluggable LLM layer.

> Repository is private and corporate-bound, so only technical approach and public patterns are shared here.

---

### Open Source Contributions

#### Forks & Branches

<!-- START_SECTION:forks -->
| Fork | Upstream | Branch | Status |
|------|----------|--------|--------|
| [phpmixbill](https://github.com/GuilhermeP96/phpmixbill) | [ibnux/phpmixbill](https://github.com/ibnux/phpmixbill) | `GuilhermeP96-patch-1`, `GuilhermeP96-patch-2` | -- |
| [ADModule](https://github.com/GuilhermeP96/ADModule) | [samratashok/ADModule](https://github.com/samratashok/ADModule) | `feature/ad-query-tool-v2` | PR Open |
| [ollama](https://github.com/GuilhermeP96/ollama) | [ollama/ollama](https://github.com/ollama/ollama) | `api`, `bmizerany/client-registry`, `bmizerany/embedspeedup` | PR Open |
| [Aios](https://github.com/GuilhermeP96/Aios) | [harshitgavita-07/Aios](https://github.com/harshitgavita-07/Aios) | `feat/sdk-streaming-hardware-aware` | PR Merged |
<!-- END_SECTION:forks -->

#### Pull Requests

<!-- START_SECTION:prs -->
| PR | Repository | Status | Date |
|----|-----------|--------|------|
| [feat: Ollama SDK integration, streaming UI, hardware-aware model selection](https://github.com/harshitgavita-07/Aios/pull/1) | harshitgavita-07/Aios | ![Merged](https://img.shields.io/badge/-Merged-8957e5) | 2026-03-27 |
| [feat: autotune - automatic hardware-based performance optimization](https://github.com/ollama/ollama/pull/15081) | ollama/ollama | ![Open](https://img.shields.io/badge/-Open-238636) | 2026-03-26 |
| [feat: Add comprehensive AD user query tool v2.0](https://github.com/samratashok/ADModule/pull/11) | samratashok/ADModule | ![Open](https://img.shields.io/badge/-Open-238636) | 2026-01-06 |
| [Added Brazilian Portuguese language.](https://github.com/GuilhermeP96/phpmixbill/pull/2) | GuilhermeP96/phpmixbill | ![Merged](https://img.shields.io/badge/-Merged-8957e5) | 2017-04-03 |
| [Brazilian Portuguese language added](https://github.com/GuilhermeP96/phpmixbill/pull/1) | GuilhermeP96/phpmixbill | ![Merged](https://img.shields.io/badge/-Merged-8957e5) | 2017-04-03 |
<!-- END_SECTION:prs -->

---

### GitHub Stats

<div align="center">
  <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=GuilhermeP96&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true" height="180" alt="GitHub Stats" />
  <img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=GuilhermeP96&layout=compact&theme=tokyonight&langs_count=10" height="180" alt="Top Languages" />
</div>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=GuilhermeP96&theme=tokyonight" alt="GitHub Streak" />
</div>

<div align="center">
  <img src="https://ghchart.rshah.org/GuilhermeP96" alt="Contribution Graph" />
</div>

---

<div align="center">

<!-- START_SECTION:stats -->
**18** public repos | **48** private repos | **9** followers | **5** PRs | **3** merged
<!-- END_SECTION:stats -->

*Last updated: 2026-08-16 16:17 UTC*

</div>
