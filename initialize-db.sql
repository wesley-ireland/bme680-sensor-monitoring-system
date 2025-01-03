-- Create the database
CREATE DATABASE bme680_sensor_monitoring_system;

-- Connect to the new database
\c bme680_sensor_monitoring_system;

-- Create tables
CREATE TABLE bme680_sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    humidity DOUBLE PRECISION NOT NULL,
    pressure DOUBLE PRECISION NOT NULL,
    gas_resistance DOUBLE PRECISION NOT NULL
);
