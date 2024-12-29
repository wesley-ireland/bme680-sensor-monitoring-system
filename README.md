# BME680 Sensor Monitoring System

A system to monitor a BME680 sensor, store the readings into a TimescaleDB real-time database, and pipe the data into a UI using Graphana for visualization.

## Setup

This project requires that you have Python installed: https://www.python.org/downloads/

You then need to create a virtual environment:

```bash
$ python -m venv myenv
```

Activate the virtual environment:

```bash
$ source myenv/bin/activate 
```

Install dependencies: 

```bash
$ pip install -r requirements.txt
```

To verify installation, you can run the following:

```bash
$ pip list
```

# Running the Script

With the setup completed, you can now run the Python script: 

```bash
$ python3 bme680_test.py
```

You will be prompted to use the real sensor or simulate:

```
To simulate, enter S, for real sensor data, enter R:
```

After which, you will start to get readings: 

```
Simulating the BME680 sensor data...
Temperature: 24.59°C
Humidity: 57.91%
Pressure: 1045.65 hPa
Gas Resistance: 37506.17 ohms
---------------------------------
Temperature: 32.29°C
Humidity: 55.55%
Pressure: 973.61 hPa
Gas Resistance: 40771.76 ohms
---------------------------------
```
