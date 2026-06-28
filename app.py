        t_cs = st.number_input("Clean Sheet", key="t_cs")
        t_t = st.number_input("Tiri medi", key="t_t")
    
    if st.button("Analizza Manuale"):
        v1, v2 = calcola_bilancia({'punti':c_p,'cs':c_cs,'tiri':c_t}, {'punti':t_p,'cs':t_cs,'tiri':t_t})
        st.info(f"Probabilità 1X: {v1:.1f}% | Probabilità X2: {v2:.1f}%")
 Partite"):
        try:
            key = st.secrets["API_FOOTBALL_KEY"]
            url = "https://v3.football.api-sports.io/fixtures?live=all"
            headers = {"x-rapidapi-key": key, "x-rapidapi-host": "v3.football.api-sports.io"}
            response = requests.get(url, headers=headers)
            data = response.json(
            
            if not data.get('response'):
                st.write("Nessuna partita live al momento.")
            
            for match in data.get('response', []):
                home = ']
                away = match[
