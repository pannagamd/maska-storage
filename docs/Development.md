# MaskaStorage — Development Guide

## Daily Development Workflow

1. **Pull latest changes** from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-feature
   ```

3. **Make changes**, committing often with Conventional Commits.

4. **Run linters** before pushing:
   ```bash
   ruff check backend/app && ruff format --check backend/app
   npm run lint --prefix frontend
   ```

5. **Push and open a PR** against `develop`.

---

## Backend Development

### Running the Server (Hot Reload)

```bash
cd backend
uvicorn app.main:app --reload
```

### Adding a New Endpoint

1. Create/modify a route file in `backend/app/api/routes/`
2. Add the corresponding Pydantic schemas in `backend/app/schemas/`
3. Register the router in `backend/app/main.py`
4. Document the endpoint in `docs/api_contract.md`

### Running Tests

```bash
cd backend
pytest -v
pytest --cov=app tests/   # With coverage
```

### Adding a New Test

Place tests in `backend/tests/` using the naming convention `test_<module>.py`.

---

## Frontend Development

### Running the Dev Server

```bash
cd frontend
npm run dev
```

### Adding a New Service

1. Create a service file in `frontend/src/services/`
2. Use `apiClient` from `apiClient.ts`
3. Add the corresponding TypeScript types to `frontend/src/types/index.ts`
4. Create a custom hook in `frontend/src/hooks/`

### Environment Variables

All frontend env vars must be prefixed with `VITE_` to be exposed to the browser bundle.

---

## Debugging

### Backend Logs

Set `LOG_LEVEL=DEBUG` in `backend/.env` for verbose logging.

### Database Queries

Set `DEBUG=true` in `backend/.env` to enable SQLAlchemy query logging.

### Docker Logs

```bash
docker compose logs -f backend
docker compose logs -f frontend
```
