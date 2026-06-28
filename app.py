import streamlit as st

 10.3")
st.title("🌡️ Termometro 10.3")

n_cs = st.text_input("Nome Casa")
p_cs = st.number_input("Punti Casa", 0.0)
t_cs = st.number_input("Tiri Casa", 0.0)
g_cs = st.number_input("Gol Casa", 0.0)
c_cs = st.number_input("Clean Sheet Casa", 0)

st.write("---")

n_os = st.text_input("Nome Ospite")
p_os = st.number_input("Punti Ospite", 0.0)
t_os = st.number_input("Tiri Ospite", 0.0)
g_os = st.number_input("Gol Ospite", 0.0)
c_os = st.number_input("Clean Sheet Ospite", 0)

if st.button("CALCOLA"):
    val_c = (p_cs * 0.1) + (t_cs * 0.1) + (g_cs * 0.8)
    if c_cs > 3: val_c *= 1.05
    
    val_o = (p_os * 0.1) + (t_os * 0.1) + (g_os * 0.8)
    if c_os > 3: val_o *= 1.05
    
    tot = val_c + val_o
    if tot > 0:
        st.metric(f"Probabilità 1X ({n_cs})", f"{(val_c/tot)*100:.1f}%")
        st.metric(f"Probabilità X2 ({n_os})", f"{(val_o/tot)*100:.1f}%")
