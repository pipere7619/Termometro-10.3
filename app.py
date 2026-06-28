import streamlit as st
import requests

# Configurazione Pagina
st.set_page_config(page_title="Termometro 10.3", layout="centered")
st.title("🌡️ Termometro 10.3")

# Funzione Analisi Match Analyst
def calcola_bilancia(dati_casa, dati_trasferta):
    p1x = 50.0
    px2 = 50.0
    
    # Calcolo ponderato
    p1x += (dati_casa['punti'] - dati_trasferta['punti']) * 1
    px2 += (dati_trasferta['punti'] - dati_casa['punti']) * 1
    p1x += (dati_casa['cs'] - dati_trasferta['cs']) * 3
    px2 += (dati_trasferta['cs'] - dati_casa['cs']) * 3
    p1x += (dati_casa['tiri'] - dati_trasferta['tiri']) * 2
    px2 += (dati_trasferta['tiri'] - dati_casa['tiri']) * 2
    
    return max(0, min(100, p1x)), max(0, min(100, px2))

# Tabs
tab1, tab2 = st.tabs(["Manuale", "API Live"])

with tab1:
    st.subheader("Inserimento Dati Manuale")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Casa")
        c_p = st.number_input("Punti", key="c_p")
        c_cs = st.number_input("Clean Sheet", key="c_cs")
        c_t = st.number_input("Tiri medi", key="c_t")
    with col2:
        st.write("Trasferta")
        t_p = st.number_input("Punti", key="t_p")
        t_cs = st.number_input("Clean Sheet", key="t_cs")
        t_t = st.number_input("Tiri medi", key="t_t")
    
    if st.button("Analizza Manuale"):
        v1, v2 = calcola_bilancia({'punti':c_p,'cs':c_cs,'tiri':c_t}, {'punti':t_p,'cs':t_cs,'tiri':t_t})
        st.info(f"Probabilità 1X: {v1:.1f}% | Probabilità X2: {v2:.1f}%")

with tab2:
    st.subheader("Analisi Live")
    if st.button("Carica Partite"):
        try:
            key = st.secrets["API_FOOTBALL_KEY"]
            url = "https://v3.football.api-sports.io/fixtures?live=all"
            headers = {"x-rapidapi-key": key, "x-rapidapi-host": "v3.football.api-sports.io"}
            response = requests.get(url, headers=headers)
            data = response.json()
            
            if not data.get('response'):
                st.write("Nessuna partita live al momento.")
            
            for match in data.get('response', []):
                home = match['teams']['home']['name']
                away = match['teams']['away']['name']
                st.write(f"⚽ **{home}** vs **{away}**")
        except Exception as e:
            st.error("Errore: Verifica che la chiave API sia nei Secrets.")
