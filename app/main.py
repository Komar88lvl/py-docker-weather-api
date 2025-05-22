import os
import requests
from weatherapi.rest import ApiException

from dotenv import load_dotenv


load_dotenv()


URL = "http://api.weatherapi.com/v1/current.json?"

CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("WEATHER_API_KEY is not set in environment variables")

    try:
        result = requests.get(
            URL + f"key={api_key}" + f"&q={CITY}"
        )

        print(result.json())
    except ApiException as e:
        print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

if __name__ == "__main__":
    get_weather()
