from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_photo(city, state):
    url = f"https://api.pexels.com/v1/search?query={city}+{state}"

    header = {
        "Authorization": PEXELS_API_KEY,
    }
    response = requests.get(url, headers=header)
    data = json.loads(response.content)
    return data["photos"][0]["src"]["medium"]


def get_coordinates(city, state):

    # header = {"Authorization": OPEN_WEATHER_API_KEY}

    coordinates_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid={OPEN_WEATHER_API_KEY}"
    coordinates_response = requests.get(coordinates_url)
    # geo_data = json.loads(coordinates_response.content)
    latitude = coordinates_response.json()[0]["lat"]
    longitude = coordinates_response.json()[0]["lon"]
    return {
        "latitude": latitude,
        "longitude": longitude,
    }


def get_weather(latitude, longitude):

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={OPEN_WEATHER_API_KEY}"
    weather_response = requests.get(weather_url)
    description = weather_response.json()["weather"][0]["description"]
    temperature = weather_response.json()["main"]["temp"]
    return {
        "description": description,
        "temperature": temperature,
    }
