import streamlit as st
import pandas as pd
from config import AppConfig

def render_dashboard():
    st.set_page_config(
        layout="wide",
        page_title="Panel pogodowy",
    )

    st.title(f"Pogoda {AppConfig.API_CITY}")