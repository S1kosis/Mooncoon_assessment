# Use a base image (e.g., Ubuntu)
FROM ubuntu:latest

# Install dependencies
RUN apt-get update && \
    apt-get install -y build-essential cmake git && \
    apt-get clean

# Clone DuckDB repository
RUN git clone https://github.com/duckdb/duckdb.git

# Build and install DuckDB
WORKDIR /duckdb
RUN git checkout v0.8.1
RUN make -j8 

# Set the working directory to /app (you can change this to your preferred directory)
WORKDIR /app

# Example: Copy a script or data into the container
# COPY your_script.py /app/

# Set the entry point to run DuckDB when the container starts
ENTRYPOINT ["duckdb"]
