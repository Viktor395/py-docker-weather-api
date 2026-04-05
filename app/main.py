import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

def get_weather():
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    url = f"{BASE_URL}?key={api_key}&q={CITY}"
    
    try:
        print(f"Performing request to Weather API for city {CITY}...")
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        local_time = data['location']['localtime']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        
        print(f"{location}/{country} {local_time} Weather: {temp_c} Celsius, {condition}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    get_weather()
