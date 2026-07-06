FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure output is displayed immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system libraries required by matplotlib and reportlab
RUN apt-get update && apt-get install -y \
    gcc \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]