from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .models import Car, Driver, Trip
from .schemas import CarCreate, DriverCreate, TripCreate
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Car CRUD operations
@app.get("/cars/")
def read_cars(db: Session = Depends(get_db)):
    cars = db.query(Car).all()
    return cars

@app.post("/cars/")
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(number=car.number, brand=car.brand, load_capacity=car.load_capacity, fuel_consumption=car.fuel_consumption)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.get("/cars/{car_id}")
def read_car(car_id: int, db: Session = Depends(get_db)):
    return db.query(Car).filter(Car.car_id == car_id).first()

# Driver CRUD operations
@app.get("/drivers/")
def read_drivers(db: Session = Depends(get_db)):
    drivers = db.query(Driver).all()
    return drivers

@app.post("/drivers/")
def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    db_driver = Driver(
        full_name=driver.full_name,
        category=driver.category
    )
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

@app.get("/drivers/{driver_id}")
def read_driver(driver_id: str, db: Session = Depends(get_db)):
    return db.query(Driver).filter(Driver.driver_id == driver_id).first()

# Trip CRUD operations
@app.post("/trips/")
def create_trip(trip: TripCreate, db: Session = Depends(get_db)):
    db_trip = Trip(
        car_id=trip.car_id,
        driver_id=trip.driver_id,
        departure_date=trip.departure_date,
        return_date=trip.return_date,
        distance=trip.distance,
        departure_point=trip.departure_point,
        destination=trip.destination
    )
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

@app.get("/trips/{trip_id}")
def read_trip(trip_id: int, db: Session = Depends(get_db)):
    return db.query(Trip).filter(Trip.trip_id == trip_id).first()
