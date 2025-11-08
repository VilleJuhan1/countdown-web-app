# Use an official lightweight Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Expose Flask port
EXPOSE 5001

# Start the app
CMD ["python", "app.py"]
