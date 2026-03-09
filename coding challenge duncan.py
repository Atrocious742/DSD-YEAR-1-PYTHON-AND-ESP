import requests

def get_coordinates(place):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": place,
        "count": 1
    }
    
    response = requests.get(url, params=params).json()
    if 'results' in response:
        latitude = response['results'][0]['latitude']
        longitude = response['results'][0]['longitude']
        return latitude, longitude
    else:
        print("Place not found!")
        return None, None

def get_hourly_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto"
    }
    
    response = requests.get(url, params=params).json()
    hourly_data = response.get('hourly', {})
    return hourly_data

place = input("Enter the name of the place: ")
latitude, longitude = get_coordinates(place)

if latitude and longitude:
    print(f"The latitude of {place} is: {latitude}")
    print(f"The longitude of {place} is: {longitude}")
    
    weather = get_hourly_weather(latitude, longitude)
    print("Hourly temperatures:", weather.get('temperature_2m', [])[:10])
    print("Hourly precipitation:", weather.get('precipitation', [])[:10])