#weather_api.py
import requests
import statistics
from datetime import date
from collections import defaultdict

api_url = "https://archive-api.open-meteo.com/v1/archive"

def get_historical_data(lat, lon, month, day):
    """(C2) Fetches daily weather data from Open-Meteor API for location, day and month over the past five years and performs aggregations"""

    current_year = date.today().year
    #five year range is 2020 through 2024 (current year -5 to current year - 1)
    years_pulled = range(current_year - 5, current_year)
    #dictionary of ALL the daily weather readings for past 5 years
    daily_values = defaultdict(list)
    # List of Open Meteo's weather API parameter names
    api_daily_params = [
        'temperature_2m_mean',
        'temperature_2m_min',
        'temperature_2m_max',
        'wind_speed_10m_mean',
        'wind_speed_10m_min',
        'wind_speed_10m_max',
        'precipitation_sum',
    ]
    #Loop through each of the 5 historical years to make separate API requests
    for year in years_pulled:
        start_date = f"{year}-{month:02d}-{day:02d}"

        # Define parameters for the HTTP GET request.
        params = {
            'latitude': lat,
            'longitude': lon,
            'start_date': start_date,
            'end_date': start_date,
            'daily': api_daily_params,  # The variables we are requesting
            'temperature_unit': 'fahrenheit', #C2 unit-fahrenheit
            'wind_speed_unit': 'mph', #C2 unit-miles per hour
            'precipitation_unit': 'inch',  # Setting the unit explicitly to inches
            'timezone': 'America/Los_Angeles' # Time Zone of Raymond, WA
        }
        #handle potential network errors
        try:
            #execute the API request via HTTP GET
            response = requests.get(api_url, params=params)
            response.raise_for_status() # stop program if status codes occur like HTTPError/RequestException
            data = response.json() #convert json into python

            if data and 'daily' in data:
                for key in api_daily_params:
                    daily_values[key].append(data['daily'][key][0]) #store in daily values dictionary at index [0]

        except requests.exceptions.RequestException as err:
            #continue loop but print exception and error message
            print(f"Sorry, there was an error fetching data for {start_date}: {err}.")

    #after loop is finished:
    if not daily_values["temperature_2m_mean"]:
        print("  ❌   Error: No successful API requests were made. Cannot calculate aggregations.")
        return None

        # Calculate and aggregate the required 5-year data (C1 variables)
    aggregated_data = {

         # Temperature (5-year Mean/Min/Max)
        'FiveYearAvgTemp': statistics.mean(daily_values['temperature_2m_mean']),
        'FiveYearMinTemp': min(daily_values['temperature_2m_min']),
        'FiveYearMaxTemp': max(daily_values['temperature_2m_max']),
        # Wind Speed (5-year Mean/Min/Max)
        'FiveYearAvgWindSpd': statistics.mean(daily_values['wind_speed_10m_mean']),
        'FiveYearMinWindSpd': min(daily_values['wind_speed_10m_min']),
        'FiveYearMaxWindSpd': max(daily_values['wind_speed_10m_max']),
        # Precipitation (5-year Sum/Min/Max) - Calculated from 5 daily sums
        'FiveYearSumPrecipitation': sum(daily_values['precipitation_sum']),
        'FiveYearMinPrecipitation': min(daily_values['precipitation_sum']),
        'FiveYearMaxPrecipitation': max(daily_values['precipitation_sum']),
        }
#return the dictionary of aggregated data to the WeatherData class
    return aggregated_data