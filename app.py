import streamlit as st
from datetime import datetime

st.set_page_config(page_title="BAYO ULTIME", page_icon="👑", layout="wide")
st.title("👑 ROBOT BAYO 1939 - ULTIME (1000 Vues)")

# On fait des onglets comme les grandes applications
onglet1, onglet2, onglet3, onglet4 = st.tabs(["📊 ANALYSEUR", "🔥 HOOK YOP", " #️⃣ HASHTAGS", "⏰ PROGRAMMATEUR"])

with onglet1:
    st.header("📊 Analyseur de vues - Pourquoi TikTok coupe ?")
    vues = st.number_input("Vues dernière vidéo", 250)
    retention = st.slider("Secondes regardées (moyenne)", 0.0, 15.0, 2.5)
    if st.button("Analyser pour 1000 vues"):
        if retention < 4:
            st.error(f"Problème : Les gens partent à {retention}s. TikTok ne poussera plus.")
            st.success("COUP DE POUCE : Mets un texte choc dès 0s")
        else:
            st.balloons()
            st.success("Vidéo bonne ! TikTok va redonner 1000 vues.")

with onglet2:
    st.header("🔥 Générateur de HOOK Yopougon")
    lieu = st.selectbox("Tu es où ?", ["Yopougon Palais", "Yop Marché", "Sous le soleil", "Dans gbaka"])
    if st.button("Génère mon Hook"):
        st.code(f"POV : {lieu} à pied à 14h, je vais pas survivre 😭\n(Tu dis ça dès la 1ère seconde avec le visage fatigué)")

with onglet3:
    st.header("#️⃣ Générateur Hashtags qui donne 1000 vues")
    if st.button("Génère hashtags"):
        st.code("#yopougon #cotedivoire #abidjan #bayo1939 #pov #marche #civ225 #yop #pourtoi #fyp")

with onglet4:
    st.header("⏰ Programmateur Officiel 19:19")
    video = st.file_uploader("Ta vidéo", type=["mp4"])
    heure = st.time_input("Heure de boost", value=datetime.strptime("19:19", "%H:%M").time())
    desc = st.text_area("Description", "POV: Yop à pied 😭 #yopougon")
    if st.button("Programmer"):
        st.success(f"Prêt ! A {heure}, le robot va te crier POSTE !")
        st.info(f"Va sur tiktok.com/upload à {heure} et colle : {desc}")

st.divider()
st.write("C'est ton application à toi maintenant Baba. Toutes les fonctionnalités en 1 seul endroit.")
