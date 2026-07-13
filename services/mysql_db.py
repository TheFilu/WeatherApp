import mysql.connector as sql
from config import AppConfig

# Funkcja tworząca połączenie z bazą
def get_connection():
    return sql.connect(
        host=AppConfig.DB_HOST,
        user=AppConfig.DB_USER,
        password=AppConfig.DB_PASSWORD,
        database=AppConfig.DB_NAME,
        use_unicode=True
    )

# Tworzenie tabeli "weather_records" jeśli nie istnieje

def create_weather_table():

    query = """
        CREATE TABLE IF NOT EXISTS weather_records (
            id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
            nazwa VARCHAR(255) NOT NULL,
            temperatura FLOAT NOT NULL,
            odczuwalna FLOAT NOT NULL,
            wilgotnosc INTEGER NOT NULL,
            cisnienie INTEGER NOT NULL,
            predkosc_wiatru FLOAT NOT NULL,
            wschod_slonca TIME NOT NULL,
            zachod_slonca TIME NOT NULL,
            opis_pogody VARCHAR(255) NOT NULL,
            timestamp DATETIME NOT NULL
        )
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabela została utworzona lub już istnieje")
    except Exception as e:
        print(e)

def save_weather_record(record):
    query = """
    INSERT INTO weather_records 
    (nazwa,temperatura,odczuwalna,wilgotnosc, cisnienie, predkosc_wiatru, wschod_slonca, zachod_slonca, opis_pogody, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        record["nazwa"],
        record["temperatura"],
        record["odczuwalna"],
        record["wilgotnosc"],
        record["cisnienie"],
        record["predkosc wiatru"],
        record["wschod slonca"],
        record["zachod slonca"],
        record["opis pogody"],
        record["timestamp"]
    )


    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def get_weather_records():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM weather_records ORDER BY timestamp DESC"

        cursor.execute(query)
        records = cursor.fetchall()

        return records

    except Exception as e:
        print(f"Wystąpił błąd podczas pobierania rekordów: {e}")
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()