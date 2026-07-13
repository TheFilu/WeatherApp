from services.openweather_api import get_weather
from services.files import save_to_file
from dashboard.home import render_dashboard
import time
from services.mysql_db import create_weather_table, save_weather_record

create_weather_table()

# render_dashboard()
#
while True:
    weather_record = get_weather()

    # [] dodane ze względu na to że, dataframe w funkcjo save_to_file potrzebuje mieć listę - nawet z jednym elementem
    save_to_file([weather_record])
    save_weather_record(weather_record)

    print("Odczyt zapisany")


    time.sleep(10)
