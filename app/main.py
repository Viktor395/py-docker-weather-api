import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        print(f"Performing request to Weather API for city {city}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"{location}/{country} {local_time} Weather: {temp_c} Celsius, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")


if __name__ == "__main__":
    get_weather()
