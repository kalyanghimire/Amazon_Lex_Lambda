#python 3.7
import json
from botocore.vendored import requests
import datetime
def lambda_handler(event, context):
    city = event["currentIntent"]["slots"]["City"]
    r = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={"q": city , "appid":"d1b248902ff7f18603fec906d81a6e93"} )
    data = r.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    output = 'Weather Information: Description: {description} Temperature: {temperature} Pressure: {pressure} Humidity: {humidity} '.format(description=description, temperature=temperature, pressure=pressure, humidity=humidity)
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": output
            }
        }
    }
