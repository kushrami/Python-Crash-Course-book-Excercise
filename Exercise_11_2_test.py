import unittest
import Excercise_11_2 as module

class CityCountry(unittest.TestCase):
    
    def test_city_country(self):
        formatted_name = module.CityCountryFunc('santiago','chille')
        self.assertEqual(formatted_name, 'santiago, chille')
    def test_city_country_population(self):
        formatted_name = module.CityCountryFunc('santiago','chille',5000000)
        self.assertEqual(formatted_name, 'santiago, chille,population - 5000000')
unittest.main()