# streamlit_app.py

import streamlit as st
import requests

# Flask API URL (yerel sunucu)
flask_url = "http://127.0.0.1:5000/summarize"

# Başlık
st.title("Metin Özetleme Uygulaması")

# Kullanıcıdan metin alma
text_input = st.text_area("Metni buraya girin:")

# Özetleme butonu
if st.button("Özetle"):
    if text_input:
        # Flask API'ye metni gönder
        response = requests.post(flask_url, json={"text": text_input})
        
        if response.status_code == 200:
            summary = response.json()["summary"]
            st.subheader("Özet:")
            st.write(summary)
        else:
            st.error("Bir hata oluştu!")
    else:
        st.warning("Lütfen bir metin girin.")
