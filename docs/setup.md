# MaskaStorage — Setup Guide

## Prerequisites

| Tool | Minimum Version |
|---|---|
| Python | 3.11+ |
| Node.js | 20+ |
| npm | 9+ |
| Docker | 24+ |
| Docker Compose | 2.20+ |
| Git | 2.40+ |

---

## 1. Clone the Repository

```bash
git clone https://github.com/your-org/maska-storage.git
cd maska-storage
```

---

## 2. Backend Setup

### 2.1 Create a virtual environment

```bash
cd backend
python -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 2.2 Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.3 Configure environment variables

```bash
cp .env.example .env
# Edit .env and fill in your actual values
```

Key variables to configure:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `OPENAI_API_KEY` | Your OpenAI API key |
| `SECRET_KEY` | A strong random secret key |
| `ALLOWED_ORIGINS` | Frontend origin URL(s) |

### 2.4 Run the backend

```bash
# From the backend/ directory
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`  
Interactive docs: `http://localhost:8000/docs`

---

## 3. Frontend Setup

### 3.1 Install dependencies

```bash
cd frontend
npm install
```

### 3.2 Configure environment variables

```bash
cp .env.example .env
# Edit .env and fill in VITE_API_BASE_URL etc.
```

### 3.3 Run the frontend dev server

```bash
npm run dev
```

The frontend will be available at: `http://localhost:5173`

---

## 4. Docker Setup (Recommended)

### 4.1 Copy environment file

```bash
cp backend/.env.example backend/.env
# Edit backend/.env as needed
```

### 4.2 Start all services

```bash
cd deployment
docker compose up --build
```

Services started:
- **Backend**: `http://localhost:8000`
- **Frontend**: `http://localhost:5173` (dev) or `http://localhost:80` (prod)
- **PostgreSQL**: `localhost:5432`
- **ChromaDB**: `http://localhost:8001`

### 4.3 Stop services

```bash
docker compose down
# To also remove volumes:
docker compose down -v
```

---

## 5. Running Tests

```bash
cd backend
pytest
```

---

## 6. Linting

```bash
# Backend (from root)
ruff check backend/app
ruff format --check backend/app

# Frontend (from root)
npm run lint --prefix frontend
```

---

## 7. Verify the Health Endpoint

```bash
curl http://localhost:8000/api/v1/health
# Expected: {"status":"ok"}
```
