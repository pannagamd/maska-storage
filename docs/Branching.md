# MaskaStorage — Branching Strategy

## Branch Overview

```
main
 └── develop
       ├── feature/add-upload-api
       ├── feature/rag-pipeline
       ├── fix/file-validation-error
       ├── docs/update-api-contract
       └── chore/upgrade-fastapi
```

---

## Branch Types

| Branch | Created From | Merged Into | Description |
|---|---|---|---|
| `main` | — | — | Production-ready code only. Protected. |
| `develop` | `main` | `main` (via release) | Integration branch for all new work. |
| `feature/<name>` | `develop` | `develop` | New features |
| `fix/<name>` | `develop` | `develop` | Bug fixes |
| `docs/<name>` | `develop` | `develop` | Documentation updates |
| `chore/<name>` | `develop` | `develop` | Tooling, CI, deps |
| `hotfix/<name>` | `main` | `main` + `develop` | Critical production patches only |

---

## Rules

1. **Never commit directly to `main` or `develop`** — always use a PR.
2. **Branch from `develop`** for all regular work.
3. **Branch from `main`** for hotfixes only.
4. **Delete the branch** after the PR is merged.
5. **Keep branches short-lived** — merge within a few days.
6. **One branch, one concern** — don't mix feature + docs + fixes in one branch.

---

## Release Process

1. Create a `release/vX.Y.Z` branch from `develop`.
2. Run full test suite and fix any issues.
3. Merge into `main` with a version tag.
4. Merge `main` back into `develop` to keep them in sync.

---

## Naming Conventions

Use lowercase and hyphens. Keep names concise but descriptive.

```bash
# Good
feature/add-health-endpoint
fix/upload-size-validation
docs/update-architecture-diagram
chore/upgrade-fastapi-0115
hotfix/critical-db-connection-leak

# Bad
feature/AddHealthEndpoint
fix/JIRA-1234
my-branch
```
