import streamlit as st

st.set_page_config(
    page_title="Java notes",
    page_icon="colapsed",
    initial_sidebar_state="collapsed",
    menu_items={}
)

def return_text(folder, file):
    with open(f"{folder}/{file}", 'r', encoding='utf-8') as file:
        caption_text = file.read()
        return caption_text

# MENU
obraz, menu = st.columns([1,5])
with menu:
    wybor = st.selectbox("Wybierz temat",("Strona główna", "JAVA", "BAZY DANYCH", "ZPI"))
with obraz:
    st.image("MENU.png", width=100)

st.divider()

if wybor == "Strona główna":
    folder = ".notes"
    st.write(return_text(folder, file="strona glowna.txt"))


elif wybor == "JAVA":
    folder = ".notes/java"
    st.header("JAVA")
    typy_danych, pojecia, metody = st.tabs(["Typy danych", "Podstawowe pojęcia", "Metody"])

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

elif wybor == "BAZY DANYCH":
    folder= ".notes/sql"

    typy_baz, pojecia, operatory, operacje, zadania = st.tabs(["Typy baz danych", "Podstawowe pojęcia", "Operatory", "Rodzaje operacji", "Zadania - lab."])
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

elif wybor == "ZPI":
    pass

