import unittest
from unittest.mock import patch, MagicMock
from weather import WeatherData
from database import WeatherRecord
from weather_api import get_historical_data

#Fake Aggregated Data:

PRETEND_DATA = {
    'FiveYearAvgTemp': 69,
    'FiveYearMinTemp': 10.0,
    'FiveYearMaxTemp': 70.0,
    'FiveYearAvgWindSpd': 5.0,
    'FiveYearMinWindSpd': 1.0,
    'FiveYearMaxWindSpd': 10.0,
    'FiveYearSumPrecipitation': 5.0,
    'FiveYearMinPrecipitation': 0.0,
    'FiveYearMaxPrecipitation': 1.5,
}

#Fake input data to test initialization:
TEST_LAT = 46.69
TEST_LON = -123.73
TEST_TEMP = 69
TEST_MONTH = 12
TEST_DAY = 25

class TestProjectLogic(unittest.TestCase):
    #1 WeatherData Class initialization (D: Test 1)
    def test_01_db_record_creation_and_mapping(self):
        """Tests that a WeatherRecord can be created and accepts all 14 fields."""
        #Create a populated data object to simulate a successful API fetch
        data = WeatherData(TEST_LAT, TEST_LON, TEST_MONTH, TEST_DAY)

        data.FiveYearAvgTemp = PRETEND_DATA['FiveYearAvgTemp']
        data.FiveYearMinTemp = PRETEND_DATA['FiveYearMinTemp']
        data.FiveYearMaxTemp = PRETEND_DATA['FiveYearMaxTemp']
        data.FiveYearAvgWindSpd = PRETEND_DATA['FiveYearAvgWindSpd']
        data.FiveYearMinWindSpd = PRETEND_DATA['FiveYearMinWindSpd']
        data.FiveYearMaxWindSpd = PRETEND_DATA['FiveYearMaxWindSpd']
        data.FiveYearSumPrecipitation = PRETEND_DATA['FiveYearSumPrecipitation']
        data.FiveYearMinPrecipitation = PRETEND_DATA['FiveYearMinPrecipitation']
        data.FiveYearMaxPrecipitation = PRETEND_DATA['FiveYearMaxPrecipitation']

        record = WeatherRecord(
            # Location and Date (C1)
            location_latitude=data.lat,
            location_longitude=data.lon,
            month=data.month,
            day_of_month=data.day,
            year=data.year,

            # Weather Aggregations (C4/C5 Mapping Check)
            five_year_avg_temp=data.FiveYearAvgTemp,
            five_year_min_temp=data.FiveYearMinTemp,
            five_year_max_temp=data.FiveYearMaxTemp,
            five_year_avg_wind_speed=data.FiveYearAvgWindSpd,
            five_year_min_wind_speed=data.FiveYearMinWindSpd,
            five_year_max_wind_speed=data.FiveYearMaxWindSpd,
            five_year_sum_precipitation=data.FiveYearSumPrecipitation,
            five_year_min_precipitation=data.FiveYearMinPrecipitation,
            five_year_max_precipitation=data.FiveYearMaxPrecipitation,
            )

            # 1c. Assertions

        self.assertEqual(record.location_latitude, TEST_LAT)
        self.assertEqual(record.five_year_avg_temp, TEST_TEMP)
        self.assertIsNotNone(record)


    # 2. Test the Class Initialization (Requirement D - Test 2)
    def test_02_class_initializes_location_data(self):
        """Tests that the WeatherData class initializes with correct location/date."""
        data = WeatherData(TEST_LAT, TEST_LON, TEST_MONTH, TEST_DAY)
        data.FiveYearAvgTemp = None

        self.assertEqual(data.lat, TEST_LAT)
        self.assertEqual(data.month, TEST_MONTH)
        self.assertIsNone(data.FiveYearAvgTemp)

    # 3. Test the API Logic (Requirement D - Test 3)
    @patch('weather_api.requests.get')
    def test_03_api_logic_calculates_aggregations(self, mock_get):
        """
        Tests the mathematical aggregation (Avg/Min/Max/Sum) logic in get_historical_data
        without connecting to the live API.
        """
        #Pretend API response data to test aggregation
        mock_response_data = {
            'daily': {
                'temperature_2m_mean': [40.0],
                'temperature_2m_min': [10.0],
                'temperature_2m_max': [70.0],
                'wind_speed_10m_mean': [5.0],
                'wind_speed_10m_min': [1.0],
                'wind_speed_10m_max': [10.0],
                'precipitation_sum': [1.0]
            }
        }

        mock_get.return_value = MagicMock(status_code=200, json=lambda: mock_response_data)

        result = get_historical_data(TEST_LAT, TEST_LON, TEST_MONTH, TEST_DAY)

        self.assertIn('FiveYearAvgTemp', result)
        self.assertEqual(result['FiveYearAvgTemp'], 40.0)
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()