from pydantic import BaseModel
from datetime import date
from typing import Optional

class CarBase(BaseModel):
    number: str
    brand: Optional[str] = None
    load_capacity: Optional[int] = None
    fuel_consumption: Optional[float] = None

class CarCreate(CarBase):
    pass

class Car(CarBase):
    car_id: int

    class Config:
        from_attributes = True

class DriverBase(BaseModel):
    full_name: str
    category: str

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    driver_id: str

    class Config:
        from_attributes = True

class TripBase(BaseModel):
    car_id: int
    driver_id: int
    departure_date: date
    return_date: date
    distance: int
    departure_point: str
    destination: str

class TripCreate(TripBase):
    pass

class Trip(TripBase):
    trip_id: int

    class Config:
        from_attributes = True
