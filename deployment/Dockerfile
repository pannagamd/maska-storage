# ============================================================
# MaskaStorage — Backend Dockerfile
# Build: docker build -t maska-backend .
# ============================================================

# ─── Stage 1: Builder ────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --target=/build/deps -r requirements.txt

# ─── Stage 2: Runtime ────────────────────────────────────
FROM python:3.11-slim AS runtime

LABEL maintainer="MaskaStorage Team"
LABEL description="MaskaStorage FastAPI backend"

# Create non-root user for security
RUN groupadd --gid 1001 maska \
    && useradd --uid 1001 --gid maska --shell /bin/bash --create-home maska

WORKDIR /app

# Copy installed deps from builder
COPY --from=builder /build/deps /usr/local/lib/python3.11/site-packages/

# Copy application source
COPY --chown=maska:maska app/ ./app/

# Create data directories
RUN mkdir -p app/data/uploads app/data/processed app/data/cache \
    && chown -R maska:maska app/data/

# Switch to non-root user
USER maska

# Expose API port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/v1/health')"

# Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
