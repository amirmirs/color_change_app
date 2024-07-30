# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY server.py server.py
COPY index.html index.html

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "server.py"]