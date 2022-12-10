import os
import streamlit as st
import pandas as pd
import requests
import json

### FUNCTIONS ###
def load_file(uploaded_file):
    # load data inside dataframe
    dataframe = pd.read_csv(uploaded_file, index_col=[0])
    st.write("L'échantillon a bien été chargé !")
    first_row = dataframe.head(1)
    # create payload
    payload = {}
    for i, col in enumerate(first_row):
        payload[first_row.columns[i]] = first_row[col][0]
    # return values for prediction      
    return payload

def send_sample(payload, server_url, headers):
    resp = requests.post(url=f"{url}/predict", json=payload, headers=headers)
    prediction = resp.text[:5]
    st.write(f"La prédiction de la résistance à 28 jours pour cet échantillon est de {prediction} MPa")

def change_is_logged_session():
    st.session_state["is_logged"] = not st.session_state["is_logged"]

### WEB APPLICATION ###
# session state
if "is_logged" not in st.session_state:
    st.session_state["is_logged"] = False

### Application ###
st.title("RC28 Prédiction")

# request params
# url = 'https://filrouge-backend.onrender.com'
url = os.environ['FASTAPI_URL']
headers = {'content-type': 'application/json'}


# login form if not logged
if st.session_state["is_logged"] == False:

    placeholder = st.empty()

    with placeholder.form("login"):
        st.markdown("#### Bonjour, veuillez renseigner vos identifiants")
        user_email = st.text_input(label="Email", placeholder="votremail@exemple.com")
        user_password = st.text_input(label="Mot de passe", placeholder="Enter votre mot de passe", type="password")
        login_button = st.form_submit_button("Login")

        if ((login_button) and (user_email == os.environ['EMAIL']) and (user_password == os.environ['PASSWORD'])):
            change_is_logged_session()
            placeholder.empty()
        elif ((login_button) and ((user_email != os.environ['EMAIL']) or (user_password != os.environ['PASSWORD']))):
            st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")

# submit sample form if logged
if st.session_state["is_logged"] == True:
    st.button("Déconnexion", on_click=change_is_logged_session)
    # loading file and sending sample for prediction
    st.text("Bienvenue, vous allez pouvoir connaitre la résistance de votre béton en un clic !")
    uploaded_file = st.file_uploader("Téléverser un fichier csv")
    if uploaded_file is not None:
        payload = load_file(uploaded_file)
        if st.button("Prédiction"):
            send_sample(payload, url, headers)