# MaskaStorage — Coding Standards

## General Principles

- **Clarity over cleverness** — write code that is easy to read and review.
- **Single Responsibility** — each module, class, and function should do one thing well.
- **No magic numbers** — use named constants from `core/constants.py` or `constants/index.ts`.
- **Error handling** — never swallow exceptions silently; always log or propagate them.
- **No dead code** — remove unused imports, variables, and commented-out code before merging.
- **TODO stubs** — stubs must include a descriptive `TODO` comment with enough context to implement.

---

## Python / Backend Standards

### Formatting & Linting

- **Formatter**: Ruff (configured in `pyproject.toml`) — `line-length = 88`.
- **Linter**: Ruff — run `ruff check backend/app` before every commit.
- **Type hints**: Required on all function signatures. Use `from __future__ import annotations` where needed.

### File Naming

- All files: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

### Docstrings

Use Google-style docstrings for all public modules, classes, and functions:

```python
def compute_hash(data: bytes, algorithm: str = "sha256") -> str:
    """
    Compute the hash of raw bytes.

    Args:
        data: The raw bytes to hash.
        algorithm: Hashing algorithm name (default: sha256).

    Returns:
        Hex-digest string.

    Raises:
        ValueError: If the algorithm is not supported.
    """
```

### Imports

Order: stdlib → third-party → local (managed by Ruff isort).

```python
# stdlib
from pathlib import Path

# third-party
from fastapi import APIRouter

# local
from app.core.config import settings
```

### Async

Use `async/await` consistently throughout the backend. Never mix sync blocking I/O in async routes.

---

## TypeScript / Frontend Standards

### Formatting & Linting

- **Formatter**: Prettier (`.prettierrc`) — `printWidth: 100`.
- **Linter**: ESLint (`.eslintrc.js`) — run `npm run lint` before every commit.
- **Types**: Strict mode enabled. Avoid `any` — use `unknown` or proper types.

### File Naming

- Components: `PascalCase.tsx` (e.g., `Layout.tsx`)
- Hooks: `camelCase.ts` prefixed with `use` (e.g., `useUpload.ts`)
- Services/utils: `camelCase.ts`
- Types: `camelCase` for interfaces/types

### Component Rules

- Functional components only (no class components).
- Props interface defined above the component.
- Components export a named export + a default export.

### Hooks Rules

- Custom hooks must start with `use`.
- Hooks manage a single concern (upload state, archive state, etc.).
- No API calls directly in components — always use a hook or service.

---

## Git Commit Standards

See [COMMIT_CONVENTION.md](../COMMIT_CONVENTION.md).

---

## Testing Standards

- **Backend**: Pytest + pytest-asyncio. Minimum: one test per public endpoint.
- **Frontend**: Vitest + React Testing Library (TODO when testing is set up).
- Tests must be deterministic and independent (no shared mutable state).
- Mock all external services (OpenAI, ChromaDB, PostgreSQL) in tests.

---

## Security Standards

- Never commit secrets, API keys, or credentials — use `.env` files.
- Validate all user inputs with Pydantic schemas.
- Sanitise filenames before storing to disk.
- Use parameterised queries via SQLAlchemy ORM — no raw SQL string interpolation.

---

## Optional Future Improvements

- Pre-commit hooks (commitlint, Ruff, ESLint) via Husky / pre-commit
- Automated dependency updates via Dependabot
- Code coverage requirements enforced in CI (e.g., 80% minimum)
