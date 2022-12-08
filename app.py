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

st.text("Bienvenue, vous allez pouvoir connaitre la RC28 en un clic !")

### file upload
uploaded_file = st.file_uploader("Téléverser un fichier csv")

if uploaded_file is not None:
    payload = load_file(uploaded_file)


### get prediction
# local_url = 'http://127.0.0.1:8000/predict'
url = 'https://filrouge-backend.onrender.com/predict'
headers = {'content-type': 'application/json'}

if st.button("send"):
    send_sample(payload, url, headers)