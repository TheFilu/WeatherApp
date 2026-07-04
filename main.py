from dashboard.home import render_dashboard
from services.openweather_api import get_weather
from services.files import save_to_file
from services.files import load_from_file
import time

df = load_from_file()
if not df.empty:
    print(df)
else:
    print("Plik jest pusty")

render_dashboard()

# while True:
#     weather_record = get_weather()
#
#     # [] dodane ze względu na to że, dataframe w funkcjo save_to_file potrzebuje mieć listę - nawet z jednym elementem
#     save_to_file([weather_record])
#
#     print(weather_record)
#
#     time.sleep(15)

