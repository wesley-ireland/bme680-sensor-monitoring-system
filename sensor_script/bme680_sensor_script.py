import time
import board
import busio
import adafruit_bme680
import random
import sys
import psycopg
import datetime

DB_HOST = "timescale-db-container"
DB_PORT = 5432
DB_NAME = "bme680_sensor_monitoring_system"
DB_USER = "postgres"
DB_PASSWORD = "password"

try:
    connection = psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit()

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

        time.sleep(2)

# user_input = input("To simulate, enter S, for real sensor data, enter R: ")
#
# if user_input == "R":
#     print("Reading the BME680 sensor data...")
#     print("---------------------------------")
#     read_bme680()
# elif user_input == "S":
#     print("Simulating the BME680 sensor data...")
#     print("---------------------------------")
#     simulate_bme680()
# else:
#     print("That is an invalid command.")
#     sys.exit()

read_bme680()
