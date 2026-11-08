import streamlit as st

from translator import translate

st.set_page_config(page_title="Перекладач", page_icon="🌐", layout="wide")

st.title("🌐 Перекладач")
st.caption(
    "Переклад тексту на обрану мову за допомогою мовної моделі (Groq). "
    "Вкажіть мову, вставте текст і отримайте лише переклад."
)

top_left, top_right = st.columns(2)
with top_left:
    api_key = st.text_input("Groq API ключ", type="password", placeholder="gsk_...")
with top_right:
    lang = st.text_input("Мова перекладу", value="українська")

left, right = st.columns(2)

with left:
    text = st.text_area("Вхідний текст", height=300)
    clicked = st.button("Перекласти", type="primary", use_container_width=True)

result = ""
if clicked:
    with st.spinner("Зачекайте..."):
        result = translate(api_key, lang, text)

with right:
    st.text_area("Переклад", value=result, height=300)
