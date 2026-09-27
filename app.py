import streamlit as st
# JAMAIS DE MOT DE PASSE ICI

# 1. Défense contre les injections
heure = st.text_input("Heure")
if not heure.isdigit(): # Tu vérifies que c'est bien un chiffre
    st.error("Mets seulement des chiffres Baba!")

# 2. Défense - Ne pas montrer les erreurs techniques
try:
    # ton code de robot
    pass
except:
    st.error("Erreur, réessaie") # Tu ne montres pas l'erreur technique au pirate
