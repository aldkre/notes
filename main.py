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
wybor = st.sidebar.selectbox("Wybierz temat",("Strona główna", "JAVA", "BAZY DANYCH", "ZPI"))

if wybor == "Strona główna":
    st.balloons()
    st.write(return_text(".notes/strona glowna.txt"))


elif wybor == "JAVA":
    # MAIN JAVA SITE
    st.header("JAVA")
    # JAVA TABS
    typy_danych, pojecia, metody = st.tabs(["Typy danych", "Podstawowe pojęcia", "Metody"])

    with typy_danych:
        typ_prymitywny, typ_referencyjny = st.columns(2)
        with typ_prymitywny:
            st.subheader("Typy prymitywne")
            st.caption(return_text('.notes/java/typy_prymitywne.txt'))

        with typ_referencyjny:
            st.subheader("Typy referencyjne")
            st.caption(return_text(".notes/java/typy_referencyjne.txt"))

        st.divider()

        st.caption(return_text(".notes/java/typy_danych_ogolnie.txt"))

    with pojecia:
        st.caption(return_text(".notes/java/pojecia.txt"))

    with metody:
        st.caption(return_text(".notes/java/metody.txt"))

elif wybor == "BAZY DANYCH":
    typy_baz, inne = st.tabs(["Typy baz danych", "Inne"])
    with typy_baz:
        st.caption(return_text(".notes/sql/typy_baz_danych.txt"))

elif wybor == "ZPI":
    pass

