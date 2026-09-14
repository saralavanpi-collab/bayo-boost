import streamlit as st
st.set_page_config(page_title="Bayo Boost", page_icon="🚀")
st.title("🚀 Bayo Boost - Coup de pouce 1000 vues")

video_desc = st.text_input("De quoi parle ta vidéo ?", placeholder="Ex: perruque blonde 30 pouces")

if st.button("Donne moi mon coup de pouce 1000 vues"):
    st.success("Plan pour atteindre 1000 vues vraies et continuer :")
    
    st.write("### 1. TON HOOK (les 2 premières secondes)")
    st.write(f"Ne commence pas par 'Salut les filles'. Commence par : 'Cette perruque {video_desc} a failli me créer des problèmes au maquis !'")
    
    st.write("### 2. TES 3 HASHTAGS MAGIQUES (Abidjan)")
    st.write("#perruqueabidjan #beaute225 #bayo1939")
    
    st.write("### 3. L'HEURE POUR POSTER")
    st.write("Poste à 19:19 ou 12:30 heure d'Abidjan. Ne poste jamais le matin.")
    
    st.write("### 4. LE TRUC SECRET POUR CONTINUER APRÈS 1000 VUES")
    st.write("Pendant les 60 premières minutes après avoir posté, tu dois répondre à TOUS les commentaires en vidéo. TikTok va voir que ta vidéo fait parler et il va la pousser à 10K.")
    
    st.warning("Fais ça sur ta prochaine vidéo et tu vas dépasser les 1000 vues. Tu me diras combien ?")
