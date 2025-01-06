import requests
import random
from faker import Faker

faker = Faker()
API_URL = "http://127.0.0.1:8000"


def generate_cars(num_cars):
    for _ in range(num_cars):
        car_data = {
            "number": faker.license_plate(),
            "brand": faker.company(),
            "load_capacity": random.randint(1000, 5000),
            "fuel_consumption": round(random.uniform(5.0, 15.0), 2),
            "color": random.choice(["Red", "Blue", "Green", "Black", "White"])
        }
        response = requests.post(f"{API_URL}/cars/", json=car_data)
        if response.status_code == 200:
            print(f"Added Car: {response.json()}")
        else:
            print(f"Failed to add Car: {response.status_code} - {response.text}")


def generate_drivers(num_drivers):
    for _ in range(num_drivers):
        driver_data = {
            "driver_id": faker.uuid4(),
            "full_name": faker.name(),
            "category": random.choice(["A", "B", "C", "D", "E"])
        }
        response = requests.post(f"{API_URL}/drivers/", json=driver_data)
        if response.status_code == 200:
            print(f"Added Driver: {response.json()}")
        else:
            print(f"Failed to add Driver: {response.status_code} - {response.text}")


def generate_trips(num_trips, car_ids, driver_ids):
    for _ in range(num_trips):
        trip_data = {
            "car_id": random.choice(car_ids),
            "driver_id": random.choice(driver_ids),
            "departure_date": faker.date_this_year().isoformat(),
            "return_date": faker.date_this_year().isoformat(),
            "distance": random.randint(50, 1000),
            "departure_point": faker.city(),
            "destination": faker.city(),
            "status": random.choice(["Scheduled", "In progress", "Complete"])
        }
        response = requests.post(f"{API_URL}/trips/", json=trip_data)
        if response.status_code == 200:
            print(f"Added Trip: {response.json()}")
        else:
            print(f"Failed to add Trip: {response.status_code} - {response.text}")


def main():
    num_cars = 100
    num_drivers = 100
    num_trips = 200

    generate_cars(num_cars)
    generate_drivers(num_drivers)

    car_response = requests.get(f"{API_URL}/cars/")
    driver_response = requests.get(f"{API_URL}/drivers/")

    if car_response.status_code == 200 and driver_response.status_code == 200:
        car_ids = [car['car_id'] for car in car_response.json()]
        driver_ids = [driver['driver_id'] for driver in driver_response.json()]

        generate_trips(num_trips, car_ids, driver_ids)
    else:
        print(f"Failed to fetch cars: {car_response.status_code} - {car_response.text}")
        print(f"Failed to fetch drivers: {driver_response.status_code} - {driver_response.text}")


if __name__ == "__main__":
    main()
