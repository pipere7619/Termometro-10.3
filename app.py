import streamlit as st
import requests

st.set_page_config(page_title="Termometro 10.3", layout="centered")

st.title("🌡️ Termometro 10.3")

# Sostituiamo il recupero dai secrets con una gestione protetta
def get_api_key():
    try:
        return st.secrets["API_FOOTBALL_KEY"]
    except:
        return None

tab1, tab2 = st.tabs(["Manuale", "API Live"])

with tab1:
    # ... (il codice del manuale che abbiamo visto prima)
    st.write("Inserisci i dati manualmente.")

with tab2:
    st.subheader("Analisi Live")
    api_key = get_api_key()
    
    if st.button("Carica Partite"):
        if not api_key:
            st.error("Errore: Chiave API non configurata nei Secrets di Streamlit.")
        else:
            with st.spinner("Connessione in corso..."):
                url = "https://v3.football.api-sports.io/fixtures"
                headers = {'x-apisports-key': api_key, 'x-rapidapi-host': "v3.football.api-sports.io"}
                querystring = {"live": "all"}
                
                try:
                    response = requests.get(url, headers=headers, params=querystring)
                    data = response.json()
                    st.write(data) # Mostra i dati grezzi per verificare la connessione
                except Exception as e:
                    st.error(f"Errore di connessione: {e}")
