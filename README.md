# Introduction to Git for Code

> **A hands-on lecture for researchers and developers — from first commit to pull request.**

This repository accompanies a lecture that teaches Git as a practical tool for managing code projects. It covers four ways to interact with Git and a full authentication walkthrough.

| Method | Tool | When to use it |
|--------|------|---------------|
| **Terminal** | `git` CLI | Full control, scripting, servers |
| **GitHub CLI** | `gh` | Pull requests, issues, repos from the terminal |
| **VS Code** | Source Control panel | Visual diffs, staging, inline blame |
| **GitHub UI** | github.com | Quick edits, reviews, project management |

## Repository contents

```
intro-to-git/
├── slides/              # Beamer lecture slides (.tex)
├── exercises/           # Hands-on exercises (progressive)
│   ├── 01-first-repo/
│   ├── 02-branching-merging/
│   ├── 03-collaboration/
│   ├── 04-conflict-resolution/
│   └── 05-gh-cli/
├── cheatsheet/          # Git & gh quick-reference (.tex)
├── sample-project/      # A small Python project to practise on
│   ├── src/
│   ├── tests/
│   └── README.md
└── .gitignore
```

## Prerequisites

- A [GitHub](https://github.com) account (free).
- Git installed (see slides for installation instructions).
- [VS Code](https://code.visualstudio.com/) with the **GitLens** extension (optional but recommended).
- [GitHub CLI (`gh`)](https://cli.github.com/) installed (covered in the lecture).

## Getting started

```bash
# Clone this repo
git clone https://github.com/YOUR-USERNAME/intro-to-git.git
cd intro-to-git

# Open in VS Code
code .
```

## Exercises

Work through these in order during or after the lecture:

| # | Exercise | You will learn |
|---|----------|---------------|
| 1 | First Repo | init, add, commit, push, .gitignore |
| 2 | Branching & Merging | branches, checkout, merge, rebase basics |
| 3 | Collaboration | fork, clone, pull, remote, pull requests |
| 4 | Conflict Resolution | merge conflicts, resolving in terminal & VS Code |
| 5 | GitHub CLI | gh repo, gh pr, gh issue, gh auth |

Each folder contains a `README.md` with step-by-step instructions and challenges.

## Authentication quick reference

| Method | Best for | Setup command |
|--------|----------|--------------|
| SSH key | Daily use (recommended) | `ssh-keygen` → add to GitHub |
| HTTPS + credential helper | Quick start | `gh auth login` or OS keychain |
| GitHub CLI token | CI / scripting | `gh auth login --with-token` |
| Personal Access Token | API / automation | Generate at github.com/settings/tokens |

## Licence

Released under the [MIT Licence](LICENSE).

---

*Prepared for the Department of Mechanical and Aeronautical Engineering, University of Pretoria.*
