import unittest
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        geolocator = get_geolocator()
        locations = ["Museum of Modern Art","USS Alabama Battleship Memorial Park"]
        return None

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsNone(result,
                          "A nonexistent location should have an empty result.")

if __name__ == "__main__":
    unittest.main()
