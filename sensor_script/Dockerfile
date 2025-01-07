# Using the official Python image as the base
FROM python:3.9

# Creating a new directory in the container
WORKDIR /app

# Copy our service files
COPY bme680_sensor_script.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "bme680_sensor_script.py"]
