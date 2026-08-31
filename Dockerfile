# Use offical python 3.13.2 image form Docker hub
FROM python:3.13.2-slim

# Set up the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 5000

# Command to run the FastAPI app
CMD ["python", "app.py"]