# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app with host=0.0.0.0 to be accessible outside the container
CMD ["python", "app.py"]
