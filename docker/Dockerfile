# 🐍 Use slim Python 3.12 base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Set working directory
WORKDIR /app

# Install OS-level dependencies for Postgres, Redis, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    curl \
    netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements for cache efficiency
COPY ../requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project
COPY .. .

# Expose FastAPI port
EXPOSE 8000

# Use uvicorn to run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
