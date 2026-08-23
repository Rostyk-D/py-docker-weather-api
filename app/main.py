import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={
            "key": api_key,
            "q": "Paris",
        },
    )
    response.raise_for_status()

    data = response.json()

    location = data["location"]
    current = data["current"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
