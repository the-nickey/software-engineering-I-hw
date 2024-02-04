import streamlit as st
from googletrans import Translator
from languages import *

st.title("Переводчик текста")
source_text = st.text_area("Введите текст для перевода:")
target_language = st.selectbox("Выберите целевой язык:", languages)
translate = st.button("Перевести")
if translate:
    translator = Translator()
    out = translator.translate(source_text, dest=target_language)
    st.write(out.text)
