import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Bayo Programmateur", page_icon="⏰")
st.title("⏰ Programmateur Yopougon - Bayo")

st.write("1. Upload ta vidéo (toi qui parles à pied)")
video = st.file_uploader("Ta vidéo", type=["mp4","mov"])

st.write("2. Heure pour poster (heure d'Abidjan)")
heure = st.time_input("Heure exacte", value=datetime.strptime("19:19", "%H:%M").time())

caption = st.text_area("Description TikTok", "POV: Marcher à Yop à pied c'est un sport 😭 #yopougon #yopcity #bayo1939")

if st.button("Programmer"):
    st.session_state['prog'] = True
    st.session_state['heure'] = heure
    st.success(f"Vidéo programmée pour {heure} ! Laisse cette page ouverte.")

if 'prog' in st.session_state:
    now = datetime.now().time()
    if now.hour == st.session_state['heure'].hour and now.minute == st.session_state['heure'].minute:
        st.balloons()
        st.error("🔥 C'EST L'HEURE DE POSTER MAINTENANT !")
        st.write(f"**Caption à copier:** {caption}")
        st.write("Ouvre TikTok et poste. Tu es à l'heure parfaite d'Abidjan.")
        # Son d'alerte
        st.audio("https://www.soundjay.com/buttons/beep-07a.wav")
    else:
        st.info(f"En attente... Il est {now.strftime('%H:%M')} - Programmé pour {st.session_state['heure']}")
        time.sleep(30)
        st.rerun()
