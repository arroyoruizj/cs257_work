-- create_cities.sql
-- author: jared arroyo ruiz

-- appropiate data types for each column in
-- the us-cities-top-1k.csv dateset


DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
city TEXT,
state TEXT,
population NUMERIC(8,0),
latitude NUMERIC(5, 2),
longitude NUMERIC(5, 2)
);
