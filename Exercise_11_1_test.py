import unittest
import Excercise_11_1 as module

class CityCountry(unittest.TestCase):
    
    def test_city_country(self):
        formatted_name = module.CityCountryFunc('santiago','chille')
        self.assertEqual(formatted_name, 'santiago, chille')

unittest.main()