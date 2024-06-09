# Weather Data Ingestion Pipeline
![weather data visuls](https://github.com/ABAYA12/weather-data-ingestion-pipeline/blob/main/visual.png)

## Project Overview
The purpose of this project is to build an end-to-end data ingestion pipeline that fetches, processes, and stores weather data from the OpenWeather API. The data pipeline is automated using Apache Airflow for scheduling and orchestration, and Docker for containerization, ensuring a scalable and consistent environment.


## Setup Instructions

### Prerequisites
- Docker
- Docker Compose
- OpenWeatherMap API Key
- Python 3.8+

### Steps
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/weather-data-ingestion.git
    cd weather-data-ingestion
    ```

2. Add your OpenWeatherMap API key to the `docker-compose.yml` file under the `data_fetcher` service.

3. Build and start the Docker containers:
    ```
    cd airflow
    docker-compose up --build
    ```

4. Access the Airflow UI at `http://localhost:8080`.

## Usage
The data fetching task runs hourly and fetches weather data for a list of predefined cities, storing the results in the PostgreSQL database.

## Fetching Weather Data
## API Key:
Ensure you have an API key from OpenWeather. Set this key directly in the docker-compose.yml under the data_fetcher service. But there is already a openweather API key there. You can generate your own key and insert it.

## Trigger the DAG:
In the Airflow web UI, trigger the weather_data_pipeline DAG to start the data ingestion process.

## Monitoring:
Monitor the progress and status of the DAG in the Airflow web UI. The DAG will fetch weather data, process it, and store it in the PostgreSQL database.

##  Accessing the Data
Connect to the Database:
Use a database client to connect to the PostgreSQL database:

1. Host: localhost
2. Port: 5432
3. User: postgres
4. Password: password
5. Database: weather

## Query the Data:
 Use SQL queries to access and analyze the weather data stored in the database.

## Directory Structure
- `airflow/`: Contains the Airflow setup and DAG definition.
- `database/`: Contains the database setup script and Dockerfile.
- `data_fetching/`: Contains the data fetching script and Dockerfile.
- `requirements.txt`: Python dependencies.
- `visualize_weather_data.py`: contains python code to visualize the weather data extracted.

## Technical Tools and Technologies
- **Python**: Scripting language.
- **PostgreSQL**: Database.
- **Docker**: Containerization.
- **Apache Airflow**: Workflow management.
- **Requests**: HTTP library for API calls.
- **Pandas**: Data manipulation library.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library.
- **Matplotlib and Seaborn**: For visualization

##Contact me:
**Mail**: ishmael@trestleacademyghana.org
