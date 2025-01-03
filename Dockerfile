# Use the official TimescaleDB image as the base
FROM timescale/timescaledb:latest-pg15

# Disabling the tuning script, as it seems to be looking for files which do not exist on the Raspberry Pi 5, crashing the container.
RUN mv /docker-entrypoint-initdb.d/001_timescaledb_tune.sh /docker-entrypoint-initdb.d/001_timescaledb_tune.sh.disabled

# Copy the initialization SQL scripts into the container
COPY initialize-db.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port
EXPOSE 5432
