# Weather Data Ingestion Pipeline

## Project Overview
This project ingests weather data from the OpenWeatherMap API and stores it in a PostgreSQL database. The pipeline is managed using Apache Airflow.

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose
- OpenWeatherMap API Key

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-data-ingestion.git
    cd weather-data-ingestion
    ```

2. Add your OpenWeatherMap API key to the `docker-compose.yml` file under the `data_fetcher` service.

3. Build and start the Docker containers:
    ```bash
    cd airflow
    docker-compose up --build
    ```

4. Access the Airflow UI at `http://localhost:8080`.

## Usage
The data fetching task runs hourly and fetches weather data for a list of predefined cities, storing the results in the PostgreSQL database.

## Directory Structure
- `airflow/`: Contains the Airflow setup and DAG definition.
- `database/`: Contains the database setup script and Dockerfile.
- `data_fetching/`: Contains the data fetching script and Dockerfile.
- `requirements.txt`: Python dependencies.

## Technical Tools and Technologies
- **Python**: Scripting language.
- **PostgreSQL**: Database.
- **Docker**: Containerization.
- **Apache Airflow**: Workflow management.
- **Requests**: HTTP library for API calls.
- **Pandas**: Data manipulation library.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library.
