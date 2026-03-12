#weather.py
# GPS OF RAYMOND WA: 46.69, -123.73
from weather_api import get_historical_data  # Ensure this path is correct in your IDE

class WeatherData:
    """Class to store location details and 5-year average weather data for past Christmases."""
    def __init__(self, lat, lon, month, day):
        #Step 1: Set variables for location and date (C1)
        self.lat = lat  #latitude
        self.lon = lon #longitude
        self.month = month #month (Christmas-12)
        self.day = day
        self.year = 2025

        #Step 2:
        #Initialize 5-year aggregated weather variables (C1)
        #All are set to None until fetch_and_set_weather_data is called.

        #temperature in fahrenheit
        self.fiveYearTemp_avg= None
        self.fiveYearTemp_min = None
        self.fiveYearTemp_max= None

        #wind speed in mph
        self.fiveYearWindSpd_avg= None
        self.fiveYearWindSpd_min = None
        self.fiveYearWindSpd_max= None

        #precipitation in inches
        self.fiveYearPrecip_sum = None
        self.fiveYearPrecip_max = None
        self.fiveYearPrecip_min = None


    def fetch_and_set_weather_data(self):
        """
        Method to call the API utility, collect the 5-year data, and
        populate all instance variables (Fulfills C2 method requirement).
        """
        # Call the utility function to get the aggregated 5-year data (C2 logic)
        data = get_historical_data(
            self.lat,
            self.lon,
            self.month,
            self.day
        )
        if data:
            # Populate all the instance variables (C1) with the aggregated results
            self.FiveYearAvgTemp = data['FiveYearAvgTemp']
            self.FiveYearMinTemp = data['FiveYearMinTemp']
            self.FiveYearMaxTemp = data['FiveYearMaxTemp']
            self.FiveYearAvgWindSpd = data['FiveYearAvgWindSpd']
            self.FiveYearMinWindSpd = data['FiveYearMinWindSpd']
            self.FiveYearMaxWindSpd = data['FiveYearMaxWindSpd']
            self.FiveYearSumPrecipitation = data['FiveYearSumPrecipitation']
            self.FiveYearMaxPrecipitation = data['FiveYearMaxPrecipitation']
            self.FiveYearMinPrecipitation = data['FiveYearMinPrecipitation']
            return True
        else:
            return False