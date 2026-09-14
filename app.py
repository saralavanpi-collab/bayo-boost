import streamlit as st
st.title("Bayo Boost @bayo1939")
st.write("Robot legal pour booster TikTok")

vues = st.number_input("Vues", value=500)
likes = st.number_input("Likes", value=50)

if st.button("Analyser"):
    taux = likes / vues * 100
    st.write(f"Taux: {taux:.1f}%")
    if taux < 5:
        st.warning("Ajoute le prix dans les 2 premieres secondes!")
    else:
        st.success("Top! Reposte meme format a 19h30")

produit = st.text_input("Produit")
prix = st.text_input("Prix")
if st.button("Generer legende"):
    st.code(f"ARRIVAGE {produit} {prix}F CFA Livraison Abidjan #abidjan #venteabidjan")
