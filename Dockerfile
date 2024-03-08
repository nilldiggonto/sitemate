# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the Gunicorn port
EXPOSE 8010

CMD python manage.py migrate && python manage.py test frontend && gunicorn --config conf/gunicorn.conf.py sitemate.wsgi --preload