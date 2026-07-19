# Conventional Commit Guidelines

MaskaStorage follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

---

## Commit Message Format

```
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```

### Rules

- **Subject line**: 72 characters max, imperative mood, lowercase, no trailing period.
- **Body**: Wrap at 100 characters. Explain *what* and *why*, not *how*.
- **Footer**: Reference issues (`Closes #123`, `Refs #456`) and breaking changes.

---

## Types

| Type | When to Use |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation-only change |
| `style` | Code style change (formatting, no logic) |
| `refactor` | Code refactor with no functional change |
| `perf` | Performance improvement |
| `test` | Adding or modifying tests |
| `chore` | Tooling, CI, build, dependencies |
| `revert` | Reverts a previous commit |
| `hotfix` | Critical production patch |

---

## Scopes

Use the area of the codebase affected. Examples:

| Scope | Area |
|---|---|
| `api` | FastAPI routes / endpoints |
| `backend` | General backend changes |
| `frontend` | General frontend changes |
| `db` | Database models or migrations |
| `ai` | AI / ML pipeline modules |
| `retrieval` | RAG / retrieval modules |
| `ci` | GitHub Actions workflows |
| `docker` | Docker / docker-compose files |
| `deps` | Dependency updates |
| `config` | Configuration / environment files |

---

## Breaking Changes

Prefix the footer with `BREAKING CHANGE:` and add a `!` after the type:

```
feat(api)!: rename /upload endpoint to /documents

BREAKING CHANGE: The /upload route has been renamed to /documents.
Update all client API calls accordingly.
```

---

## Examples

```bash
# New feature
feat(api): add GET /api/v1/health endpoint

# Bug fix with issue reference
fix(upload): handle missing file extension gracefully

Closes #42

# Documentation
docs(setup): add Docker installation instructions

# Dependency update
chore(deps): upgrade fastapi to 0.115.0

# Breaking change
feat(chat)!: replace query param with request body

BREAKING CHANGE: The /chat endpoint now accepts a JSON body instead of
query parameters. Update all API client calls.
```
