FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps required for some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy project
COPY . /app

# Upgrade pip and install Python deps
RUN pip install --upgrade pip
RUN pip install -r hrms-backend/requirements.txt

EXPOSE 8000

# Start the FastAPI app; Render will set $PORT
CMD ["sh", "-c", "cd hrms-backend && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
