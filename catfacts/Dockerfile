# Use an official Python runtime as a parent image
FROM python:3.12.0-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
