import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Marketing - Streamlit",
    page_icon="./logo-python.png",
    layout="wide",
)

st.title("Votre Dashboard interactif avec Streamlit 🎨")

st.subheader("Bienvenue sur votre Dashboard")

st.write("Bienvenue sur notre plateforme interactive qui vous permettra d'explorer et d'analyser des données de manière intuitive. Ce Dashboard a été spécialement conçu pour vous aider à mieux comprendre les concepts clés de la data science et à acquérir une expérience pratique en utilisant Streamlit.")


st.subheader("Comment utiliser `Streamlit` ?")
st.write("Voici les quelques commandes de base pour utiliser `Streamlit` :")


df = pd.read_csv('data.csv')

st.subheader("Affichage des donnees brutes")
if st.checkbox("Afficher les données brutes"):
    st.write(df)


col1, col2 = st.columns(2)


st.subheader("Affichage dynamique des donnees")
with col1:
    profession = list(df.Profession.value_counts().index)
    st.write("1️⃣ Example de widget")
    age = st.slider("Sélectionnez un âge", min_value=20, max_value=100, value=30, step=1)
    pro = st.selectbox('Sélectionnez une profession', profession)
    st.write(df[(df.Profession == pro) & (df.Age > age)])


with col2:
    st.write("2️⃣ Example de widget formulaire")

    column = ['Graduated', 'Ever_Married']
    option = ['Yes', 'No']
    age_user = range(100)
    nb_children = range(14)

    form = st.form(key='my_form')

    with form:
        c1 = st.selectbox('Sélectionnez un crière', column)
        c2 = st.selectbox('Sélectionnez une option', option)
        c3 = st.selectbox('Sélectionnez un âge', age_user)
        c4 = st.selectbox('Sélectionnez un nombre d\'enfant', nb_children)

        submit = form.form_submit_button(label='Submit')

        if submit:
            st.write(df[(df[c1] == c2) & (df.Family_Size > c3)].Work_Experience.mean())


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write("filename:", uploaded_file.name)
    st.write(df)

st.sidebar.title("Menu")
