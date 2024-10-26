import streamlit as st

st.set_page_config(
    page_title="Java notes",
    page_icon="colapsed",
    initial_sidebar_state="collapsed",
    menu_items={}
)

def return_text(file):
    with open(file, 'r', encoding='utf-8') as file:
        caption_text = file.read()
        return caption_text

# SIDEBAR
with st.sidebar:
    pass

# MAIN JAVA SITE
st.header("JAVA")

typy_danych, pojecia, metody = st.tabs(["Typy danych", "Podstawowe pojęcia", "Metody"])

with typy_danych:
    typ_prymitywny, typ_referencyjny = st.columns(2)
    with typ_prymitywny:
        st.subheader("Typy prymitywne")
        st.caption(return_text('.notes/typy_prymitywne.txt'))

    with typ_referencyjny:
        st.subheader("Typy referencyjne")
        st.caption(return_text(".notes/typy_referencyjne.txt"))

    st.divider()

    st.caption(return_text(".notes/typy_danych_ogolnie.txt"))

with pojecia:
    st.caption(return_text(".notes/pojecia.txt"))

with metody:
    st.caption(return_text(".notes/metody.txt"))

