# Pull the official base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Entrypoint script to wait for db
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]


