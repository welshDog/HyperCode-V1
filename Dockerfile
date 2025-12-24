# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY pyproject.toml setup.py README.md ./
COPY src/ ./src

# Install package in development mode with all dependencies
RUN pip install --user -e ".[dev]"

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy only the installed Python packages from the builder
COPY --from=builder /root/.local /root/.local
# Copy the application code
COPY --from=builder /app /app

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Create a non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["hypercode"]
