import streamlit as st

from translator import translate

st.set_page_config(page_title="Перекладач", page_icon=":material/translate:", layout="wide")

st.markdown(
    """
    <style>
    div.stButton > button { width: 100%; background-color: #2563eb; border: none; }
    div.stButton > button:hover { background-color: #1d4ed8; }
    div.stButton > button p { color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Перекладач")
st.caption("Вкажіть мову, вставте текст і отримайте переклад.")

top_left, top_right = st.columns(2)
with top_left:
    api_key = st.text_input("Groq API ключ", type="password", placeholder="gsk_...")
with top_right:
    lang = st.text_input("Мова перекладу", value="українська")

left, right = st.columns(2)

with left:
    text = st.text_area("Вхідний текст", height=280)
    clicked = st.button("Перекласти")

result = ""
if clicked:
    with st.spinner("Зачекайте..."):
        result = translate(api_key, lang, text)

with right:
    st.text_area("Переклад", value=result, height=280)
