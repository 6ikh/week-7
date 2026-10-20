'''
Script to load geographical data into a pandas DataFrame, and save it as a CSV file.
'''

from geopy.geocoders import Nominatim
import pandas as pd


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    return Nominatim(user_agent=agent)

def fetch_location_data(geolocator, loc):
    """
    Fetch latitude, longitude, and location type for a given location string
    """
    try:
        location = geolocator.geocode(loc)
        if location is None:
            return None
        return {
            "location": loc, "latitude": location.latitude, "longitude": location.longitude, "type": location.geo_type}
    except Exception:
        return None

def build_geo_dataframe(geolocator, locations):
    """
    Build a pandas DataFrame containing geographical data for a list of locations
    """
    geo_data = [
        fetch_location_data(geolocator, loc) for loc in locations
    ]
    valid_geo_data = [item for item in geo_data if item is not None]
    return pd.DataFrame(valid_geo_data)


if __name__ == "__main__":
    geo = get_geolocator()

    locations = ["Museum of Modern Art", "iuyt8765(*&)", "Alaska", "Franklin's Barbecue", "Burj Khalifa"]

    df = build_geo_dataframe(geo,locations)

    df.to_csv("./geo_data.csv")
