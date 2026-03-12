# main.py
#imports
from weather import WeatherData
from database import WeatherRecord, create_database_session
import sys
from sqlalchemy import select

#main function/define variables:
RAYMOND_LAT = 46.69
RAYMOND_LON = -123.73
EVENT_MONTH = 12 # December
EVENT_DAY = 25   # CHRISTMAS!

def save_weather_data(event_data):
    """
    Populates SQLite table with the weather data aggregated.
    """
    #1 Create database session, connect to database file (C5 setup)
    session = create_database_session()
    #2 Create instance of database record (WeatherRecord, part C4)
    #Map the data to database fields:
    new_record = WeatherRecord(
        #Location and Date
        location_latitude=event_data.lat,
        location_longitude=event_data.lon,
        month=event_data.month,
        day_of_month=event_data.day,
        year=event_data.year,
        #five year temp
        five_year_avg_temp=event_data.FiveYearAvgTemp,
        five_year_min_temp=event_data.FiveYearMinTemp,
        five_year_max_temp=event_data.FiveYearMaxTemp,
        #five year wind speed
        five_year_avg_wind_speed=event_data.FiveYearAvgWindSpd,
        five_year_min_wind_speed=event_data.FiveYearMinWindSpd,
        five_year_max_wind_speed=event_data.FiveYearMaxWindSpd,
        #five year precipitation (sum)
        five_year_sum_precipitation=event_data.FiveYearSumPrecipitation,
        five_year_max_precipitation=event_data.FiveYearMaxPrecipitation,
        five_year_min_precipitation=event_data.FiveYearMinPrecipitation,
    )
    #3 Add new record and commit to database (C5)
    try:
        session.add(new_record)
        session.commit()
        #success prints
        print("          🗄                                           ")
        print("              🗃️                              ")
        print("            🗂️                       ")
        print("                 💾                ")
        print()
        print()
        print("Data successfully saved to weather.db (C5)!")
        print()
        print()
        print()
        return True
    except Exception as e:
        #rollback transaction and exit program on database fail
        session.rollback()
        #print error message
        print()
        print(f" ❌ Error ❌ : There was a problem saving to database: {e}")
        #exit program
        session.close()
        sys.exit(1)

    finally:
        session.close()


def query_weather_data():
    """
    Queries SQLite table for weather data and prints it
    """
    #C6
    #Create a database session:
    session = create_database_session()

    try:
        #fix 3: changed order of limit 1 to happen before the ordering.
        #fix 2: added limit 1 to make sure just the newest record is returned
        #fix 1: added sort by descending feature
        stmt = select(WeatherRecord).limit(1).order_by(WeatherRecord.id.desc())

        result = session.execute(stmt).scalar_one_or_none()
        retrieved_record = result

        if retrieved_record:
            # Printing the formatted data to the screen (c6)

            print(f"DATABASE QUERY RESULTS FOR:   🗂  💾️ ")
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print(f"  🌎  Location: Raymond, WA")
            print(f"  🧭  South West Washington Coast")
            print(f"  📍  Coordinates: Latitude: {retrieved_record.location_latitude}, Longitude: {retrieved_record.location_longitude}")
            print(f"  🗓️  Date: {retrieved_record.month}/{retrieved_record.day_of_month}/{retrieved_record.year} (Historical Collection)")
            print()
            print(f"  🤔  Question: What was the weather of Christmases Past?  🎄  ❓  ")
            print(f"==============================================================================")
            print(f"<><><><><><><<><><><><><><><><><><><><><><><><><><>><>><><><><><><>><><><><>")
            print(f" Temperature (Fahrenheit) Aggregations (5 year):   🌡️    ☀️   ⚡   ❄️    🌡️    ")
            print(f"      Average: {retrieved_record.five_year_avg_temp:.2f}°F")
            print(f"      Minimum: {retrieved_record.five_year_min_temp:.2f}°F")
            print(f"      Maximum: {retrieved_record.five_year_max_temp:.2f}°F")
            print("____________________________________________________________________________")
            print(f" Wind Speed (MPH) Aggregations (5 year):.  `  .  🌬️ .  ~  💨 '  . 🍃 . `  🌀  .  `")
            print(f"      Average: {retrieved_record.five_year_avg_wind_speed:.2f} mph")
            print(f"      Minimum: {retrieved_record.five_year_min_wind_speed:.2f} mph")
            print(f"      Maximum: {retrieved_record.five_year_max_wind_speed:.2f} mph")
            print("____________________________________________________________________________")
            print(f" Precipitation (Inches) Aggregations (5 year):  🌦️    💧    🌧️   🌩️   🌨️    ❄️")
            print(f"       Total Sum: {retrieved_record.five_year_sum_precipitation:.2f} in")
            print(f"       Min Daily: {retrieved_record.five_year_min_precipitation:.2f} in")
            print(f"       Max Daily: {retrieved_record.five_year_max_precipitation:.2f} in")
            print(f"<><><><><><><<><><><><><><><><><><><><><><><><><><>><>><><><><><><>><><><><>")
            print(f"==============================================================================")
            print()
            print()
            print(f" ☁️  ☁️  ☁️  🌨️  ☁️  🌨️   ☁️  ☁️  🌨️ ☁️  ☁️  🌨️ 🌨️☁️  🌨️ 🌨️ 🌨️☁️  🌨️  🌨   ️🌨 ☁️ ☁️ ☁️ 🌨️  ☁️ 🌨️ 🌨️   ")
            print(f"   ❄️         ❄️           ❄️       ❄️        ❄️          ❄️       ❄️     ❄️        ❄️       ")
            print(f"      I'm           ❄️           ❄️             ❄️                      ❄️       ")
            print(f"            ❄️  Dreaming                  ❄️             ❄️         ❄️        ")
            print(f"     ❄️                   ❄️  of           ❄️                ❄️            ❄️         ")
            print(f"   ❄️         ❄️       ❄️        ❄️    a          ❄️         ❄️                 ❄️      ")
            print(f"                    ❄️     ❄   ❄️        ❄️   White       ❄️        ❄️     ❄️      ")
            print(f"         ❄️    ️                      ❄️              ❄️  🎅🏾   Christmas   🎄     ❄️     ️")
            print(f"       ❄️    ️   ❄️    ❄️                  ❄️      ❄️         ❄️              ❄️")
            print(f"             ❄️         ❄️       ❄️     ❄️   ...but I won't get my hopes up.   ❄️    ️")

            return True
        else:
            #print error message if fail retrieving data
            print(f" ⚠️ Uh Oh! Query failed: No data found in the database.")
            return False

    except Exception as e:
        # print error message if error is pulled
        print(f"⚠️ ❌Error❌: There was a problem during database query: {e}")
        return False

def main():
    """
    Main execution function for fetching weather data and saving it to the database.
    """

    #create class C3 instance with global variables:

    event_data = WeatherData(
        lat=RAYMOND_LAT,
        lon=RAYMOND_LON,
        month=EVENT_MONTH,
        day=EVENT_DAY,
    )
    #initialize instance
    print()
    print(f". . . . . .Hello and Welcome to Josie's Weather API!. . . . . . .")
    print()
    print(f"---*Initializing Data Collection for Raymond, WA ({EVENT_MONTH}/{EVENT_DAY})*---")

    #C2 step: pull daily weather variables and check success
    fetch_success = event_data.fetch_and_set_weather_data()

    if fetch_success:
        #C5: save the data to the SQLite database
        print(" 🌈 !Success! Data aggregation results fetched!")
        save_success=save_weather_data(event_data)

        if save_success:
            #ready for C6: Query data and print the formatted results
            query_success = query_weather_data()
            if query_success:
                #success prints
                print("Database successfully populated and ready for Query! 🗂️ ")
                print()
                print()
        else:
            print("Uh oh! 😢  Program failed to retrieve data. Cannot Proceed  🚷 ")
            print()

#start 'er up!
#program start point

if __name__ == "__main__":
    main()


