import streamlit as st

st.set_page_config(page_title="Bayo Boost", page_icon="🚀")

st.title("🚀 Bayo Boost @bayo1939")
st.subheader("Robot légal pour visibilité TikTok")

compte = st.text_input("Nom du compte TikTok à analyser", value="@bayo1939", help="Tu peux mettre @bayo1939 ou @un_autre_compte")

col1, col2 = st.columns(2)
with col1:
    vues = st.number_input("Vues de la dernière vidéo", min_value=0, value=500)
with col2:
    likes = st.number_input("Likes de la dernière vidéo", min_value=0, value=50)

if st.button("🔍 Analyser la visibilité", use_container_width=True):
    if vues == 0:
        st.warning("Mets les vues de ta dernière vidéo")
    else:
        taux = (likes / vues * 100) if vues > 0 else 0
        
        st.divider()
        st.write(f"### Résultat pour {compte} :")
        st.metric("Taux d'engagement", f"{taux:.1f}%")

        if taux < 3:
            st.error("🚨 Ton taux est FAIBLE. TikTok ne pousse pas ta vidéo.")
            st.write("**Solution pour + de visibilité:**")
            st.write("1. Change ton HOOK (les 2 premières secondes) : Commence par 'Regarde ce que j'ai trouvé...'")
            st.write("2. Reposte la vidéo à **19h30 Heure d'Abidjan** - c'est l'heure où les gens scrollent le plus")
            st.write("3. Mets 3 hashtags max: #abidjan #tiktokci #pourtoi")
        elif taux < 8:
            st.warning("⚠️ C'est MOYEN. Tu peux faire 3x plus de vues.")
            st.write("**Solution:** Ta vidéo est bonne mais la fin est faible. Finis avec une question: 'Tu veux la partie 2 ?'")
        else:
            st.success("🔥 EXCELLENT ! Ton contenu perce ! Poste une suite aujourd'hui à 12h30 et 19h30.")

        st.info(f"💡 Conseil pour {compte}: Poste 1 vidéo par jour à 12h30 et 19h30 (Heure d'Abidjan). C'est là que TikTok CI est le plus actif.")
        
        st.divider()
        st.write("**Compare avec un autre compte:**")
        st.write(f"Tu viens d'analyser {compte}. Maintenant efface et mets le nom d'un concurrent qui a beaucoup de vues, mets ses vues/likes et clique Analyser pour voir pourquoi lui il perce.")

st.caption("Fait par Baba - 100% légal, pas de fausses vues")
