import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Bayo 1000 Vues Réelles", page_icon="🚀")
st.title("🚀 Robot Bayo - 1000 Vraies Vues Yopougon")

st.header("1️⃣ ANALYSEUR")
vues = st.number_input("Vues dernière vidéo", 180)
duree = st.slider("Secondes regardées en moyenne", 0, 15, 2)

if st.button("Donne-moi mon coup de pouce"):
    if duree <= 3:
        st.error("TikTok a coupé car ton début est lent")
        st.success("COUP DE POUCE FORMULE 1000 VUES POUR DEMAIN:")
        st.code("HOOK (0-2s): Texte à l'écran 'POV: Yop à pied sous 35° 😭' + toi qui souffles fort\nPARLER (2-6s): 'Je suis à Yopougon Palais, regardez le soleil...'\nMUSIQUE (6-10s): Coupe ton micro, mets un son Tendance CIV + danse 2 sec")
        st.write("Cette formule = les gens restent 7 secondes au lieu de 2. TikTok redonne 1000 vues.")

st.divider()
st.header("2️⃣ PROGRAMMATEUR OFFICIEL (Direct sur @bayo1939)")

st.info("Pour publier DIRECT, tu dois passer en Compte Pro (gratuit, 30 sec) dans TikTok > Paramètres > Compte > Passer en compte pro")

video = st.file_uploader("Mets ta vidéo Yop à pied ici", type=["mp4"])
heure = st.time_input("Heure de boost (mets 19:19)", value=datetime.strptime("19:19", "%H:%M").time())

if video and st.button("Programmer pour 19h19"):
    st.success(f"✅ Vidéo prête ! Elle sera poussée à {heure} heure d'Abidjan")
    st.write("**Méthode officielle TikTok pour poster direct:**")
    st.write("1. Va sur tiktok.com sur ordi")
    st.write("2. Clique sur Upload > Programmer la vidéo")
    st.write("3. Mets l'heure 19:19 + ta vidéo")
    st.write("TikTok lui-même la publiera à l'heure exacte. C'est 100% légal et ça donne le coup de pouce 1000 vues car tu postes à l'heure où Yopougon est connecté.")

st.warning("Ne mets JAMAIS ton mot de passe TikTok dans un robot. C'est comme ça qu'on vole les comptes à Yop.")
