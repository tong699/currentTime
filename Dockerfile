# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your app code
COPY main.py .

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the port Uvicorn will run on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
