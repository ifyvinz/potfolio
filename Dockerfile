# Base image for Python
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app/portfolio_backend
WORKDIR /app/portfolio_backend

# Install system dependencies for PostgreSQL (even if using SQLite, it's good practice)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file from the root directory to the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY wait-for-it.sh /usr/bin/wait-for-it
RUN chmod +x /usr/bin/wait-for-it


# Copy the entire Django project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "portfolio_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
