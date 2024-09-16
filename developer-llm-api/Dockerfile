# Use a lightweight Python base image
FROM python:3.9-slim

# Set environment variables to avoid Python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary dependencies
RUN apt-get update && apt-get install -y curl
RUN apt-get remove nano

# Uninstall any old version of the openai library
RUN pip uninstall -y openai

# Install the latest version of the openai library and flask
RUN pip install --upgrade openai flask

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY developer_llm.py /app/

# Run the Python script
CMD ["python", "developer_llm.py"]
