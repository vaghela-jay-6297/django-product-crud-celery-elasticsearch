# Dockerfile
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Add this to your Dockerfile
COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# Update the CMD to use the entrypoint script
CMD ["/app/entrypoint.sh"]