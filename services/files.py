import pandas as pd
#import openpyxl potrzebny tylko do instalacji, można skasowaźć linijkę
from config import AppConfig
import os

EXT = AppConfig.FILE_EXTENSION
PATH = AppConfig.FILE_PATH

def save_to_file(data):
    new_df = pd.DataFrame(data)
    file_path = f"{PATH}.{EXT}"

    if os.path.exists(file_path):
        # odczytaj istniejący plik
        current_df = pd.read_excel(file_path)
        # połącz stare z nowym
        final_df = pd.concat([current_df, new_df])
    else:
        # przypisz nowe do finalnego df
        final_df = new_df

    if EXT == "xlsx":
        final_df.to_excel(file_path, index=False)
    elif EXT == "csv":
        final_df.to_csv(file_path, index=False)
    else:
        print("Rozszerzenie nie jest wspierane")


def load_from_file():
    file_path = f"{PATH}.{EXT}"

    if not os.path.exists(file_path):
        print("Nie istnieje")
        return None
    if EXT == "xlsx":
        return pd.read_excel(file_path)
    elif EXT == "csv":
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

