DROP TABLE IF EXISTS Trip;
DROP TABLE IF EXISTS Driver;
DROP TABLE IF EXISTS Car;

CREATE TABLE Car (
    car_id SERIAL PRIMARY KEY,
    number VARCHAR(10) NOT NULL,
    brand VARCHAR(50),
    load_capacity INTEGER,
    fuel_consumption DECIMAL(5, 2)
);

CREATE TABLE Driver (
    driver_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    category CHAR(1)
);

CREATE TABLE Trip (
    trip_id SERIAL PRIMARY KEY,
    car_id INTEGER REFERENCES Car(car_id) ON DELETE CASCADE,
    driver_id INTEGER REFERENCES Driver(driver_id) ON DELETE CASCADE,
    departure_date DATE,
    return_date DATE,
    distance INTEGER,
    departure_point VARCHAR(50),
    destination VARCHAR(50)
);
