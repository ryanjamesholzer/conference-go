from .keys import PEXELS_API_KEY
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
