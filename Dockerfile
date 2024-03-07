FROM python:3.11-slim

# Set my programs directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV APP_NAME SimpleCalculator

# Run app.py when the container launches
CMD ["python", "simplecalculator.py"]