import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter your city name: \n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}"

    weather_data = requests.get(request_url).json()

    print(f"\nCurrent weather for {weather_data["name"]}")
    print(f"\nTemp is for {weather_data["main"]["temp"]}")
    print(f"\nFeels Like is for {weather_data["main"]["feels_like"] and {weather_data["weather"][0]["description"]}}.")

if __name__ == "__main__":
    get_current_weather()