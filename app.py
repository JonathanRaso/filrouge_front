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

def send_login(email, password):
    payload = {'email': email, 'password': password}
    resp = requests.post(url=f"{url}/login", json=payload, headers=headers)
    return resp

def send_sample(payload, server_url, headers):
    resp = requests.post(url=f"{url}/predict", json=payload, headers=headers)
    prediction = resp.text[:5]
    st.write(f"La prédiction de la résistance à 28 jours pour cet échantillon est de {prediction} MPa")

def change_is_logged_session():
    st.session_state["is_logged"] = not st.session_state["is_logged"]


st.title("Test")
st.write(os.environ['PWD'])
st.write(os.environ['EMAIL'])
st.text(os.environ['PWD'])
st.text(os.environ['EMAIL'])
st.write(os.getenv(PWD))
st.write(os.getenv(EMAIL))
st.text(os.getenv(PWD))
st.text(os.getenv(EMAIL))


# session state
if "is_logged" not in st.session_state:
    st.session_state["is_logged"] = False

### Application ###
st.title("RC28 Prédiction")

# request params
# url = 'http://127.0.0.1:8000'
url = 'https://filrouge-backend.onrender.com'
headers = {'content-type': 'application/json'}


# login form
if st.session_state["is_logged"] == False:

    placeholder = st.empty()

    with placeholder.form("login"):
        st.markdown("#### Bonjour, veuillez renseigner vos identifiants")
        user_email = st.text_input(label="Email", placeholder="votremail@exemple.com")
        user_password = st.text_input(label="Mot de passe", placeholder="Enter votre mot de passe", type="password")
        login_button = st.form_submit_button("Login")

        if ((login_button) and (user_email == os.environ['EMAIL']) and (user_password == os.environ['PWD'])):
            change_is_logged_session()
            placeholder.empty()
        elif ((login_button) and ((user_email != os.environ['EMAIL']) or (user_password != os.environ['PWD']))):
            st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")

if st.session_state["is_logged"] == True:
    st.write(st.session_state["is_logged"])
    # st.write(user_email, user_password)
    # print(user_email, user_password)
    st.button("Déconnexion", on_click=change_is_logged_session)
    
    # loading file and sending sample for prediction
    st.text("Bienvenue, vous allez pouvoir connaitre la résistance de votre béton en un clic !")
    uploaded_file = st.file_uploader("Téléverser un fichier csv")
    if uploaded_file is not None:
        payload = load_file(uploaded_file)
        if st.button("Prédiction"):
            send_sample(payload, url, headers)






        # if login_button:
        #     access_granted = send_login(user_email, user_password)
        #     if access_granted != "Connexion autorisée":
        #         print(f"retour api = pas {access_granted}")
        #         st.session_state["is_logged"]
        #         change_is_logged_session()
        #         st.session_state["is_logged"]
        #         placeholder.empty()
        #     else:
        #         st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")

            # if access_granted == "Connexion autorisée":
            #     change_is_logged_session()
            #     placeholder.empty()
            # else:
            #     st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")

        # if ((login_button) and (user_email == usermail) and (user_password == password)):
        #     change_is_logged_session()
        #     placeholder.empty()
        # elif ((login_button) and ((user_email != usermail) or (user_password != password))):
        #     st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")








##################### CHECK WHY SESSIONS DOESNT WORK WHEN DEPLOYED
# usermail = "testmail@le1817.com"
# password = "granulo"

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

# st.text("Bienvenue, vous allez pouvoir connaitre la résistance de votre béton en un clic !")
# uploaded_file = st.file_uploader("Téléverser un fichier csv")
# if uploaded_file is not None:
#     payload = load_file(uploaded_file)

#     if st.button("Prédiction"):
#         send_sample(payload, url, headers)