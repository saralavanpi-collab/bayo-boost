import streamlit as st
st.set_page_config(page_title="Bayo Boost", page_icon="🚀")
st.title("🚀 Bayo Boost - Espion @bayo1939")

ta_niche = st.selectbox("Ta niche", ["Beauté / Perruques", "Mode / Vêtements", "Business"])
compte_concurrent = st.text_input("Compte concurrent à copier", value="@aziz.la.naiguaso7")
vues = st.number_input("Vues de sa vidéo qui a percé", value=1700000)

if st.button("Adapter sa stratégie à ma niche"):
    st.success(f"Analyse de {compte_concurrent} : {vues} vues")
    st.write(f"### Stratégie pour ta niche : {ta_niche}")
    
    if "Beauté" in ta_niche:
        st.write("**1. VIDÉO À FAIRE DEMAIN (copie exacte de sa formule):**")
        st.write("   Titre: 'Quand tu sors avec la perruque de ton voisin 😭'")
        st.write("   Action: 0-2sec tu montres perruque moche qui s'envole (drôle) -> 2-5sec tu mets TA perruque et tu danses comme lui.")
        st.write("**2. SON:** Utilise le même son que sa vidéo à 1.7M")
        st.write("**3. Heure:** Poste à 19:19 (heure où il poste souvent) - Heure Abidjan")
    
    st.info("Astuce de pro: Épingle comme lui tes 3 meilleures vidéos en haut de ton profil TikTok @bayo1939")
