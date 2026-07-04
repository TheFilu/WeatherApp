import requests
from datetime import datetime
from config import AppConfig
from common.functions import convert_temp
from common.functions import convert_speed

API_KEY = AppConfig.API_KEY
API_CITY = AppConfig.API_CITY

def get_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}"

    try:
        res = requests.get(URL)
        data = res.json()
        weather = {
            "nazwa": data.get("name"),
            "temperatura": convert_temp(data.get("main").get("temp"), 'C'),
            "odczuwalna": convert_temp(data.get("main").get("feels_like"), 'C'),
            "wilgotnosc": data.get("main").get("humidity"),
            "cisnienie": data.get("main").get("pressure"),
            "predkosc wiatru": convert_speed(data.get("wind").get("speed")),
            "wschod slonca": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S"),
            "zachod slonca": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S"),
            "opis pogody": data.get("weather")[0].get("description"),
            "timestamp": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }
        return weather
    except Exception as e:
        print(e)
