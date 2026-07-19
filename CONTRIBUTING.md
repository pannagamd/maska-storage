# Contributing to MaskaStorage

Thank you for your interest in contributing to **MaskaStorage**! 🎉
This document outlines the process for contributing code, documentation, and ideas.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Branching Strategy](#branching-strategy)
5. [Commit Convention](#commit-convention)
6. [Pull Request Process](#pull-request-process)
7. [Reporting Issues](#reporting-issues)

---

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a welcoming and harassment-free environment for all contributors.

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/maska-storage.git
   cd maska-storage
   ```
3. **Set up** the development environment following [docs/setup.md](docs/setup.md).
4. **Create a branch** from `develop` (see [Branching Strategy](#branching-strategy)).

---

## Development Workflow

- Always branch from `develop`, not `main`.
- Write clear, focused commits following the [Conventional Commits](COMMIT_CONVENTION.md) spec.
- Keep PRs small and focused on a single concern.
- Add or update tests for any logic you introduce.
- Run the linters before opening a PR:
  ```bash
  # Backend
  ruff check backend/app
  ruff format --check backend/app

  # Frontend
  npm run lint --prefix frontend
  ```

---

## Branching Strategy

| Branch pattern | Purpose |
|---|---|
| `main` | Production-ready code only |
| `develop` | Integration branch for in-progress work |
| `feature/<name>` | New features (branch from `develop`) |
| `fix/<name>` | Bug fixes (branch from `develop`) |
| `docs/<name>` | Documentation updates |
| `chore/<name>` | Tooling, CI, dependency updates |
| `hotfix/<name>` | Critical production patches (branch from `main`) |

---

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/). See [COMMIT_CONVENTION.md](COMMIT_CONVENTION.md) for full details.

**Examples:**
```
feat(api): add GET /health endpoint
fix(upload): handle empty file upload gracefully
docs(setup): update Python version requirements
chore(ci): add backend lint workflow
```

---

## Pull Request Process

1. Ensure your branch is up-to-date with `develop`.
2. Open a PR against `develop` (not `main`).
3. Fill out the PR template completely.
4. Ensure all CI checks pass.
5. Request a review from at least one team member.
6. Address all review comments before merging.
7. Squash commits if requested by the reviewer.

---

## Reporting Issues

- Use the [GitHub Issues](../../issues) tab.
- Use the appropriate issue template (Bug Report / Feature Request).
- Provide as much context as possible.
- Search existing issues before opening a new one.
