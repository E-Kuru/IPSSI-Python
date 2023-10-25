import streamlit as st
import pandas

df = pandas.read_csv("data.csv")

# Configuration de la page
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🧊",
    layout="wide"
)

# Titre de la page
st.title("Hello World!")

# Sous-titre de la page
st.subheader("This is a subheader")

# Texte
st.text("Hello Streamlit!")

# Checkbox
if st.checkbox("Show dataframe"):
    st.write(df)

# Columns 
col1, col2, col3 = st.columns(3)
with col1:
    st.title("Col 1")
    # Selectbox
    number = st.selectbox("Choississez un nombre", ['France', 'Espagne', 'Italie'])
    st.write("Vous avez choisi le nombre", number)



with col2:
    st.title("Col 2")

    # Input user
    user_input = st.text_input("Entrez votre nom")
    st.write("Vous avez entré", user_input)

    # Slider
    age = st.slider("Entrez votre âge", 1, 100)
    st.write("Vous avez", age, "ans")


with col3:
    st.title("Col 3")
    form = st.form(key="my_form")

    with form:
        st.title("My Form")
        bouton = st.form_submit_button(label="Submit")

        if bouton:
            st.write('Moyenne des âges :', df.Age.mean())


# Sélectionner les lignes dont l'âge est supérieur à 50 et les Hommes
st.write(df[(df.Age > 50) & (df.Gender == 'Male')])