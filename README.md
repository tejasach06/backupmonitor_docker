# BackupMonitor Docker Variant

**BackupMonitor** is a Python application designed to retrieve backup status information from a MariaDB database and present it in an easy-to-understand format. This README provides instructions for deploying the application using both Docker and Docker Compose.

## Features

- **Get Backup Status:** Fetches backup details based on provided start and end dates.
- **User Interface (HTML):** Utilizes Flask framework to render HTML templates for displaying results.
- **SQL Queries:** Demonstrates fetching data from a database using SQL queries.

## Installation

1. **Install Docker and Docker Compose:**
   - **Docker:** Download and install from [Docker's official website](https://docs.docker.com/engine/install/).
   - **Docker Compose:** Follow the [official installation guide](https://docs.docker.com/compose/install/).

2. **Clone the Repository:**
   ```bash
   git clone https://gitlab.com/docker_projects4470835/backupmonitor_docker
   ```
   Navigate to the project directory:
   ```bash
   cd backupmonitor_docker
   ```

## Docker

1. **Build the Docker Image:**
   ```bash
   docker build -t backupmonitor .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 8000:8000 --env DB_HOST=<your_db_host> --env DB_USER=<your_db_user> --env DB_NAME=<your_db_name> --env DB_PASSWORD=<your_db_password> backupmonitor
   ```
   Replace `<your_db_host>`, `<your_db_user>`, `<your_db_name>`, and `<your_db_password>` with your MariaDB database credentials.

## Docker Compose

1. **Configure Docker Compose:**

   Create or modify the `docker-compose.yml` file with the following content:

   ```yaml
   version: '3.8'

   services:
     dr_backup:
       build: .
       image: dr_monitor
       ports:
         - "8000:8000"
       environment:
         DB_HOST: # IP or hostname of DB server
         DB_USER: # Username
         DB_NAME: # Name of database to use
         DB_PASSWORD: # Password
       container_name: BackupMonitor
   ```

2. **Build and Run Using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

## How to Run

- **With Docker:** Access the application at `http://localhost:8000/` (replace `localhost` with your desired IP address or hostname if needed).
- **With Docker Compose:** Access the application at `http://localhost:8000/` (replace `localhost` with your desired IP address or hostname if needed).

## Development Server (Debug Mode)

For development purposes, you can run the Flask application in debug mode. Ensure your Flask application is configured for debug mode in `backup_tracker.py`. Use Docker or Docker Compose as described above to build and run the container.

## Notes

- Ensure you have MariaDB database credentials (host, username, password, database name) properly configured in either the Docker run command or `docker-compose.yml` file.
- Modify the `index()` function in the `backup_tracker.py` file to include data fetching logic tailored to your specific backup jobs and their statuses, such as "success" or "failed".

## Non Docker variant

For more information and source code, visit: [BackupMonitor GitLab Repository](https://gitlab.com/python515015/backupmonitor)

