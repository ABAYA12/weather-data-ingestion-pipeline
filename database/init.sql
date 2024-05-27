CREATE DATABASE weather;
\c weather

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    description VARCHAR(255),
    datetime TIMESTAMP
);
