import streamlit as st
import pandas as pd
from config import AppConfig


def render_dashboard():
    st.set_page_config(
        layout="wide",
        page_title="Panel pogodowy",
    )
    # Wczytywanie danych
    df = pd.read_csv("warszawa_weather.csv")
    # Konwersja daty
    df["timestamp"] = df["timestamp"].replace("/","-")

    # Poprawka (mamy nie do końca poprawny zapis daty, używamy "/" lepsze są myślniki "-")
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        format="mixed",
        dayfirst=True
    )
    df["wschod slonca"] = pd.to_datetime(df["wschod slonca"])
    df["zachod slonca"] = pd.to_datetime(df["zachod slonca"])


    # Podstawowe informacje ---------------------------------------------------
    st.title(f"Pogoda {AppConfig.API_CITY}")
    st.write(f"Analiza danych pogodowych dla miasta {AppConfig.API_CITY} w 2026 roku")

    # Sidebar ------------------------------------------------------------------
    st.sidebar.header("Filtry i ustawienia")

    # Zakres dat
    min_date = df["timestamp"].min()
    max_date = df["timestamp"].max()
    date_range = st.sidebar.date_input(
        "Wybierz zakres dat",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date,
    )

    # Przefiltrowanie naszego df, aby pasował do dat
    if len(date_range) == 2:
        # rozpakowanie listy, żebym nie musiał pisac nazwa[0], nazwa[1]
        start_date, end_date = date_range

        df_filtered = df[
            (df["timestamp"] >= pd.to_datetime(start_date)) &
            (df["timestamp"] <= pd.to_datetime(end_date))
        ]

    else:
        df_filtered = df.copy()


    # Metryki z informacjami --------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Średnia temperatura", f"{df_filtered["temperatura"].mean():.2f} C")
    col2.metric("Maksymalna temperatura", f"{df_filtered["temperatura"].max():.2f} °C"),
    col3.metric("Średnia wilgotność", f"{df_filtered["wilgotnosc"].mean():.2f}")
    col4.metric("Liczba rekordów", len(df_filtered))

    st.divider()
    #  Wykres temperatury -------------------------------------------

    st.subheader("Temperatura w czasie")

    temp_data = df_filtered.set_index("timestamp")["temperatura"]

    st.line_chart(
        temp_data,
    )

    # Dwie kolumny z wykresami

    left, right = st.columns(2)

    with left:
        st.subheader("Wilgotność")
        humidity_data = df_filtered.set_index("timestamp")["wilgotnosc"]
        st.area_chart(humidity_data)
    with right:
        st.subheader("Prędkość wiatru")
        wind_data = df_filtered.set_index("timestamp")["predkosc wiatru"]
        st.bar_chart(wind_data)

    # Analiza miesięczna ---------------------------

    st.subheader("Średnie wartosci miesieczne")

    df_filtered["miesiac"] = df_filtered["timestamp"].dt.month

    monthly_data = df_filtered.groupby("miesiac").agg({
        "temperatura": "mean",
        "wilgotnosc": "mean",
        "predkosc wiatru": "mean",
    }).round(2)

    #Tworzenie tabeli z danymi ze zmiennej mothly_data
    st.line_chart(monthly_data, use_container_width=True)

    #Najcieplejsze dni -------------------------------
    st.subheader("Najcieplejsze dni")

    top_hot_days = df_filtered.sort_values("temperatura", ascending=False).head(10)
    st.dataframe(
        top_hot_days[
            [
                "timestamp",  # DO POPRAWY
                "temperatura",
                "odczuwalna",
            ]
        ],
        use_container_width=True
    )


