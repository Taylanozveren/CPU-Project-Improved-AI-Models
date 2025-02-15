# Dockerfile for cpu_scheduler_project
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY . /app/

# Default command
CMD ["python", "main.py"]
