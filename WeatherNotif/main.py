import os
import requests
import json
from pynotifier import Notification

weather_api_key = os.environ.get("WEATHER_API_KEY")

city_name = "London"

url = (
    "https://api.weatherapi.com/v1/forecast.json?key="
    + weather_api_key
    + "&q="
    + city_name
)

response = requests.get(url)
print(json.dumps(response.json(), indent=2))

response_value = response.json()
print(type(response_value))

location = response_value["location"]["name"]
temp = response_value["current"]["temp_c"]
condition = response_value["current"]["condition"]["text"]

notif_text = (
    "For "
    + location
    + ", temprature is "
    + str(temp)
    + " degrees Celsius."
    + "\n"
    + "The condition is "
    + condition
    + "."
)

Notification(
    title="Weather",
    description=notif_text,
    duration=10,
    urgency="normal",
).send()
