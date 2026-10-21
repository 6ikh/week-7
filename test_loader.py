import unittest
from loader import *
import pandas as pd

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        """ Test that valid locations return a non-empty DataFrame """
        geolocator = get_geolocator()
        # locations variable is defined
        locations = ["Museum of Modern Art","USS Alabama Battleship Memorial Park"]
        df = build_geo_dataframe(locations,geolocator)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertEqual(len(df), len(locations))

        for column in ["location", "latitude", "longitude", "type"]:
            self.assertIn(column, df.columns)

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")
        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertTrue(pd.isna(result["latitude"]))
        self.assertTrue(pd.isna(result["longitude"]))
        self.assertTrue(pd.isna(result["type"]))

if __name__ == "__main__":
    unittest.main()
