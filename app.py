import os
import streamlit as st
import pandas as pd
import requests
import json

### Functions ###
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
    resp = requests.post(url=url, json=payload, headers=headers)
    prediction = resp.text[:5]
    st.write(f"La prédiction de la résistance à 28 jours pour cet échantillon est de {prediction} MPa")

### Application ###
st.title("RC28 Prédiction")

### file upload
# uploaded_file = st.file_uploader("Téléverser un fichier csv")

# request params
url = 'https://filrouge-backend.onrender.com/predict'
headers = {'content-type': 'application/json'}

##################### CHECK WHY SESSIONS DOESNT WORK WHEN DEPLOYED
# usermail = "testmail@le1817.com"
# password = "granulo"

# # Initialization
# if "logged" not in st.session_state:
#     st.session_state["logged"] = False


# # login form
# if st.session_state["logged"] == False:

#     placeholder = st.empty()

#     with placeholder.form("login"):
#         st.markdown("#### Bonjour, veuillez renseigner vos identifiants")
#         user_email = st.text_input(label="Email", placeholder="votremail@exemple.com")
#         user_password = st.text_input(label="Mot de passe", placeholder="Enter votre mot de passe", type="password")
#         login_button = st.form_submit_button("Login")

#         if ((login_button) and (user_email == usermail) and (user_password == password)):
#             st.session_state["logged"] = True
#             placeholder.empty()
#         elif ((login_button) and ((user_email != usermail) or (user_password != password))):
#             st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")
# else:
#     if st.button("Déconnexion"):
#         del st.session_state["logged"]
# # loading file and sending sample for prediction
# if st.session_state["logged"]:
#     st.text("Bienvenue, vous allez pouvoir connaitre la résistance de votre béton en un clic !")
#     uploaded_file = st.file_uploader("Téléverser un fichier csv")
#     if uploaded_file is not None:
#         payload = load_file(uploaded_file)

#         if st.button("Prédiction"):
#             send_sample(payload, url, headers)
##################### CHECK WHY SESSIONS DOESNT WORK WHEN DEPLOYED


# loading file and sending sample for prediction

st.text("Bienvenue, vous allez pouvoir connaitre la résistance de votre béton en un clic !")
uploaded_file = st.file_uploader("Téléverser un fichier csv")
if uploaded_file is not None:
    payload = load_file(uploaded_file)

    if st.button("Prédiction"):
        send_sample(payload, url, headers)