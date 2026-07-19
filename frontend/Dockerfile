# ============================================================
# MaskaStorage — Frontend Dockerfile
# Build: docker build -t maska-frontend -f frontend/Dockerfile .
# ============================================================

# ─── Stage 1: Builder ────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files for layer caching
COPY package*.json ./

# Install all dependencies (including devDependencies for build)
RUN npm ci --quiet

# Copy source code
COPY . .

# Build the production bundle
RUN npm run build

# ─── Stage 2: Runtime (Nginx) ────────────────────────────
FROM nginx:1.25-alpine AS runtime

LABEL maintainer="MaskaStorage Team"
LABEL description="MaskaStorage React frontend served by Nginx"

# Copy built assets from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose HTTP port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
