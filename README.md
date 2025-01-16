# BME680 Sensor Monitoring System

A system to monitor a BME680 sensor, store the readings into a TimescaleDB real-time database, and pipe the data into a UI using Graphana for visualization.

## Prerequisites

You should have Docker installed on your machine. If you have an older version of Docker (< 20.10.0), ensure you also have Docker Compose installed, as it is likely not bundled with your version of Docker. 

## Running the System

With the setup completed, you can now run the containers with Docker Compose:

```bash
$ docker compose up -d
```

After which, you should have 3 containers running: 

1. `sensor-script-container`: A python script that connects to your BME680 sensor and is taking readings over the GPIO and I2C protocol. This script also connects via the established Docker Compose default network to your TimescaleDB, and is performing writes to the database with the sensor data.
2. `timescale-db-container`: A TimescaleDB instance, with a table for storing sensor data. 
3. `grafana-container`: A Grafana website, exposed on port 3000.

## Viewing the Real-Time Data in Grafana

todo explain how to set up the dashboard
