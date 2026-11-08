import streamlit as st

from translator import translate

st.set_page_config(page_title="Перекладач", page_icon=":material/translate:", layout="wide")

st.markdown(
    """
    <style>
    .block-container { max-width: 1100px; padding-top: 2.5rem; }
    .header { display: flex; align-items: center; justify-content: center; gap: 1rem; }
    .logo { display: flex; align-items: center; justify-content: center; width: 3.4rem; height: 3.4rem; border-radius: 16px; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #ffffff; font-size: 1.5rem; font-weight: 700; box-shadow: 0 6px 16px rgba(79, 70, 229, 0.35); }
    .title { font-size: 2.6rem; font-weight: 800; margin: 0; }
    .subtitle { text-align: center; opacity: 0.7; margin: 0.4rem 0 2rem 0; }
    div.stButton > button { width: 100%; height: 3rem; font-size: 1.05rem; font-weight: 600; border-radius: 10px; }
    textarea { font-size: 1rem !important; }
    .footer { text-align: center; opacity: 0.5; font-size: 0.85rem; margin-top: 2.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="header"><div class="logo">A文</div><div class="title">Перекладач</div></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Вкажіть мову, вставте текст і отримайте лише переклад.</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    top_left, top_right = st.columns(2)
    with top_left:
        api_key = st.text_input("Groq API ключ", type="password", placeholder="gsk_...")
    with top_right:
        lang = st.text_input("Мова перекладу", value="українська")

left, right = st.columns(2)

with left:
    with st.container(border=True):
        text = st.text_area("Вхідний текст", height=280, placeholder="Вставте текст тут...")
        clicked = st.button("Перекласти", type="primary")

result = ""
if clicked:
    with st.spinner("Зачекайте..."):
        result = translate(api_key, lang, text)

with right:
    with st.container(border=True):
        st.text_area("Переклад", value=result, height=280, placeholder="Тут з'явиться переклад")
        st.markdown("")

st.markdown(
    '<div class="footer">Мовна модель: Groq, openai/gpt-oss-120b</div>',
    unsafe_allow_html=True,
)
