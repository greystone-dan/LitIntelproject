# Multi-stage Dockerfile for AI CaseLibrary Backend
# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies for Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# Stage 2: Runtime
FROM python:3.12-slim AS runtime

WORKDIR /app

# Install runtime dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 appuser

# Copy Python packages from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PATH="/home/appuser/.local/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.getenv('PORT', '8000') + '/health', timeout=5)" || exit 1

# Run uvicorn server bound to 0.0.0.0 without the development reloader.
ENV PORT=8000
CMD ["sh", "-c", "exec uvicorn backend.main:app --host 0.0.0.0 --port \"$PORT\""]
