#database.py

from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the Base class required by SQLAlchemy's ORM
Base = declarative_base()

class WeatherRecord(Base):
    """
    Second class to create a table in SQLite using SQLAlchemy ORM (C4).
    Defines the database schema to store all aggregated weather data.
    """
    # Define the table name
    __tablename__ = 'weather_data'

    # Primary Key (C4)
    id = Column(Integer, primary_key=True)

    # Location and Date Fields (C4, matching C1 variables)
    location_latitude = Column(Float)
    location_longitude = Column(Float)
    month = Column(Integer)
    day_of_month = Column(Integer)
    year = Column(Integer)

    # 5-Year Aggregated Weather Fields (C4, matching C1 variables)

    # Temperature (Fahrenheit)
    five_year_avg_temp = Column(Float)
    five_year_min_temp = Column(Float)
    five_year_max_temp = Column(Float)

    # Wind Speed (mph)
    five_year_avg_wind_speed = Column(Float)
    five_year_min_wind_speed = Column(Float)
    five_year_max_wind_speed = Column(Float)

    # Precipitation (inches) - Sum, Min, and Max are required (C4)
    five_year_sum_precipitation = Column(Float)
    five_year_min_precipitation = Column(Float)
    five_year_max_precipitation = Column(Float)


# --- Utility Functions for Database Setup (Used in C5) ---
def create_database_session(db_path='weather.db'):
    """Creates the SQLite engine, the table, and returns a session to interact with the database."""

    # Create the database file connection engine. This will create 'weather.db' if it doesn't exist. If program gives error: "Multiple Rows were found when one or none was required", delete this file and try again.
    engine = create_engine(f'sqlite:///{db_path}')

    # Create the 'weather_data' table in the database file (if it doesn't exist)
    Base.metadata.create_all(engine)

    # Return a session factory for database interactions
    Session = sessionmaker(bind=engine)
    return Session()