# Base image for Python
FROM python:3.10-slim

# Set environment variables to prevent Python from buffering stdout and stdin
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "portfolio_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
