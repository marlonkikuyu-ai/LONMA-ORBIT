FROM python:3.12.8-slim

WORKDIR /app

# System dependencies needed for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ← Change this line to match your actual start command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
