import streamlit as st
from PIL.Image import Image

st.set_page_config(
    page_title="Java notes",
    page_icon="🐦",
    initial_sidebar_state="collapsed",
    menu_items={}
)

def return_text(folder, file):
    with open(f"{folder}/{file}", 'r', encoding='utf-8') as file:
        caption_text = file.read()
        return caption_text

# MENU
wybor = st.selectbox("Wybierz temat",("Strona główna", "JAVA", "BAZY DANYCH", "ZPI"))

st.divider()

if wybor == "Strona główna":
    folder = ".notes"
    st.write(return_text(folder, file="strona glowna.txt"))


elif wybor == "JAVA":
    folder = ".notes/java"
    st.header("JAVA")
    typy_danych, pojecia, metody, zadania, wejsciowki = st.tabs(["Typy danych", "Podstawowe pojęcia", "Metody", "Zadanie - lab.", "Wejściówki"])

    with typy_danych:
        typ_prymitywny, typ_referencyjny = st.columns(2)
        with typ_prymitywny:
            st.subheader("Typy prymitywne")
            st.caption(return_text(folder, file="typy_prymitywne.txt"))

        with typ_referencyjny:
            st.subheader("Typy referencyjne")
            st.caption(return_text(folder, file="typy_referencyjne.txt"))

        st.divider()

        st.caption(return_text(folder, file="typy_danych_ogolnie.txt"))

    with pojecia:
        st.caption(return_text(folder, file="pojecia.txt"))

    with metody:
        st.caption(return_text(folder, file="metody.txt"))

    with zadania:
        st.caption(return_text(folder, file="zadania lab.txt"))

    with wejsciowki:
        url = 'https://github.com/aldkre/notes/blob/d369b0fcd76eda5cce6277850b9457d00ae1c1c4/.notes/java/k1_solved.jpg'
        st.page_link(url, label="Rozwiązanie", icon="🐾")
        st.caption(return_text(folder, file="kartkowka 1.txt"))

elif wybor == "BAZY DANYCH":
    folder= ".notes/sql"

    typy_baz, pojecia, operatory, operacje, zadania, wejsciowki = st.tabs(["Typy baz danych", "Podstawowe pojęcia", "Operatory", "Rodzaje operacji", "Zadania - lab.", "Wejściówki"])
    with typy_baz:
        st.caption(return_text(folder, file="typy_baz_danych.txt"))

    with pojecia:
        st.caption(return_text(folder, file="pojecia.txt"))

    with operatory:
        st.caption(return_text(folder, file="operatory.txt"))

    with operacje:
        st.caption(return_text(folder, file="operacje_sql.txt"))

    with zadania:
        st.caption(return_text(folder, file="zadania lab.txt"))

    with wejsciowki:
        st.caption(return_text(folder, file="kartkowka 1.txt"))

elif wybor == "ZPI":
    pass

