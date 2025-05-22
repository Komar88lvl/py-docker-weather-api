import os
import requests

from dotenv import load_dotenv


load_dotenv()


URL = "http://api.weatherapi.com/v1/current.json?"

CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("WEATHER_API_KEY is not set in environment variables")

    result = requests.get(
        URL + f"key={api_key}" + f"&q={CITY}"
    )

    print(result.json())


if __name__ == "__main__":
    get_weather()
