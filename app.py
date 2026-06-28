streamlit as st
import requests

st.set_page_config(page_title="Termometro 10.3", layout="cent
st.title("🌡️ Termometro 10.3")

# Sostituiamo il recupero dai secrets con una gestione protetta
def get_api_key():
    try:
        return st.secrets["API_FOOTBALL_KEY"]
    except:
        return None

 in corso..."):
                url = "https://v3.football.api-sports.io/fixtures"
                headers = {'x-apisports-key': api_key, 'x-rapidapi-host': "v3.football.api-sports.io"}
                querystring = {"live": "all"}
                
                try:
                    response = requests.get(url, headers=headers, params=querystring)
                    da
