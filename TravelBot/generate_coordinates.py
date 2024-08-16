import pandas as pd
import requests

# Load the original CSV file
itinerary_df = pd.read_csv("itinerary_events.csv")

# Your Google Maps Geocoding API key
API_KEY = 'AIzaSyChJQSPakT4mt9ipri9X905f-4YONfcSG8'

def get_lat_long(location):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            location_data = data['results'][0]['geometry']['location']
            return location_data['lat'], location_data['lng']
    return None, None

# Add latitude and longitude columns
itinerary_df['latitude'], itinerary_df['longitude'] = zip(*itinerary_df['location'].apply(get_lat_long))

# Save the updated dataframe to a new CSV file
itinerary_df.to_csv("itinerary_events_with_coordinates.csv", index=False)
