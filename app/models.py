from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL, CHAR
from sqlalchemy.orm import relationship
from .database import Base

class Car(Base):
    __tablename__ = 'car'

    car_id = Column(Integer, primary_key=True, index=True)
    number = Column(String(10), nullable=False)
    brand = Column(String(50))
    load_capacity = Column(Integer)
    fuel_consumption = Column(DECIMAL(5, 2))

class Driver(Base):
    __tablename__ = 'driver'

    driver_id = Column(String(25), primary_key=True, unique=True)
    full_name = Column(String(100))
    category = Column(CHAR(1))

class Trip(Base):
    __tablename__ = 'trip'

    trip_id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey('car.car_id', ondelete='CASCADE'))
    driver_id = Column(String(25), ForeignKey('driver.driver_id', ondelete='CASCADE'))
    departure_date = Column(Date)
    return_date = Column(Date)
    distance = Column(Integer)
    departure_point = Column(String(50))
    destination = Column(String(50))

    car = relationship("Car", back_populates="trips")
    driver = relationship("Driver", back_populates="trips")
