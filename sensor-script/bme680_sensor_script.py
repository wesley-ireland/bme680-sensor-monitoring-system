import signal
import time
import board
import busio
import adafruit_bme680
import random
import sys
import psycopg
import datetime
import os

print("Waiting a bit for the database to start. Please hold...")
time.sleep(10)

try:
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = connection.cursor()
    print("Connected to the database.")
except Exception as e:
    print(f"Error connecting to database: {e}")
    sys.exit()

def insert_sensor_reading(timestamp, sensor):
    try:
        query = """
        INSERT INTO bme680_sensor_data (timestamp, temperature, humidity, pressure, gas_resistance) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (timestamp, sensor.temperature, sensor.humidity, sensor.pressure, sensor.gas))
        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")

def simulate_bme680():
    while True:
        temperature = round(random.uniform(20, 35), 2)
        humidity = round(random.uniform(30, 70), 2)
        pressure = round(random.uniform(950, 1050), 2)
        gas_resistance = round(random.uniform(5000, 50000), 2)

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Gas Resistance: {gas_resistance} ohms")
        print("---------------------------------")

        time.sleep(2)

def read_bme680():
    # Set up I2C communication
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x76)

    while True:
        # Print temperature, humidity, pressure, and gas resistance
        print(f"Temperature: {sensor.temperature:.2f} C")
        print(f"Humidity: {sensor.humidity:.2f} %")
        print(f"Pressure: {sensor.pressure:.2f} hPa")
        print(f"Gas Resistance: {sensor.gas:.2f} ohms")
        print("-------------------------------------")

        now = datetime.datetime.now(datetime.timezone.utc)
        insert_sensor_reading(now, sensor)

        time.sleep(0.5)

# When container stops, docker sends SIGTERM to the main process, which we need to handle, otherwise the container takes
# 10s to shut down and is sent a SIGKILL signal.
def handle_sigterm(signum, frame):
    print("SIGTERM received. Closing database connection and exiting application.")
    if connection:
        connection.close()
    sys.exit(0)
signal.signal(signal.SIGTERM, handle_sigterm)

# Run main method
read_bme680()
