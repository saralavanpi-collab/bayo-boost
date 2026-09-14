import streamlit as st

st.set_page_config(page_title="Bayo Boost", page_icon="🚀")
st.title("🚀 Bayo Boost @bayo1939")
st.subheader("Robot d'espionnage légal TikTok")

# TA NICHE
ta_niche = st.selectbox("Ta niche à toi c'est quoi ?", 
    ["Mode / Vêtements", "Beauté / Perruques / Maquillage", "Accessoires / Sacs", "Humour / Divertissement", "Business / Motivation", "Autre"])

st.divider()

# COMPTE A ANALYSER
compte = st.text_input("Compte TikTok à analyser (toi ou un concurrent)", value="@bayo1939")
col1, col2 = st.columns(2)
with col1:
    vues = st.number_input("Vues de sa dernière vidéo", value=50000)
with col2:
    likes = st.number_input("Likes de sa dernière vidéo", value=5000)

if st.button("🔍 Espionner & Adapter à ma niche", use_container_width=True):
    taux = (likes / vues * 100) if vues > 0 else 0
    st.divider()
    st.write(f"### Analyse de {compte} : {taux:.1f}% d'engagement")
    
    if taux >= 8:
        st.success(f"Ce compte PERCE. Voici comment copier sa stratégie pour ta niche : **{ta_niche}**")
        
        if "Mode" in ta_niche:
            st.write("**À COPIER pour toi:**")
            st.write("1. **HOOK à copier:** Lui commence par '3 tenues que...' -> Toi fais '3 tenues avec 1 pagne qui...'")
            st.write("2. **Montage à copier:** Il montre vite 3 looks -> Toi fais pareil en 7 secondes")
            st.write("3. **Appel à l'action:** Il dit 'Quelle tenue tu préfères ?' -> Parfait pour toi aussi")
        
        elif "Beauté" in ta_niche:
            st.write("**À COPIER pour toi:**")
            st.write("1. **HOOK à copier:** Lui fait une transformation Avant/Après -> Toi fais 'Perruque à 15k vs 50k, la différence ?'")
            st.write("2. **Secret:** Il montre le résultat à la fin -> Garde le suspens 5 sec avant de montrer la perruque")
            st.write("3. **Phrase qui fait vendre sans vendre:** 'Les filles qui savent, savent'")

        else:
            st.write(f"**À COPIER pour ta niche {ta_niche}:**")
            st.write("1. Copie son HOOK (les 2 premières secondes)")
            st.write("2. Copie sa durée (si sa vidéo fait 7 sec et perce, fais 7 sec)") 
            st.write("3. Adapte avec ton vocabulaire: remplace son sujet par un sujet de ta niche")

        st.info(f"💡 ACTION MAINTENANT pour {ta_niche}: Reprends sa vidéo qui a {vues} vues et refais-la version {ta_niche}. Poste aujourd'hui à 19h30 heure Abidjan.")

    else:
        st.error(f"Ce compte {compte} ne perce PAS en ce moment ({taux:.1f}%). Ne copie pas ça.")
        st.write(f"Pour ta niche **{ta_niche}**, poste plutôt une vidéo qui pose une question à la fin.")

st.caption("Fait par Baba - Espionnage légal 100% TikTok CI").  import streamlit as st
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
