# Dockerfile

# Use the official Python image as a base
FROM python:3.9-slim

# Set a working directory for the app
WORKDIR /app

# Copy requirements.txt and the rest of the app into the container
COPY requirements.txt requirements.txt
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on (port 80)
EXPOSE 443

# Define the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app on port 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=443"]