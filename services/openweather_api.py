import requests
from datetime import datetime

API_KEY = 'f736cd8749351f7146d3599927302472'
API_CITY = 'Dąbrowa Górnicza'

def get_weather():
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}&units=metric'

    try :
        res = requests.get(URL)
        data = res.json()
        weather = {
            "nazwa" : data.get('name'),
            "temperatura" : data.get('main').get('temp'),
            "odczuwalna temperatura" : data.get('main').get('feels_like'),
            "wilgotność" : data.get('main').get('humidity'),
            'ciśnienie' : data.get('main').get('pressure'),
            'prędkość wiatru' : data.get('wind').get('speed'),
            'zachód słońca' : datetime.fromtimestamp(data.get('sys').get('sunset')).strftime('%H:%M'),
            'wschód słońca' : datetime.fromtimestamp(data.get('sys').get('sunrise')).strftime('%H:%M'),
            'aktualna godzina' : datetime.now().strftime('%H:%M')
        }
        print(weather)
    except Exception as e:
        print(e)
