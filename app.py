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
url = 'http://127.0.0.1:8000/predict'
headers = {'content-type': 'application/json'}

if st.button("send"):
    send_sample(payload, url, headers)





# if uploaded_file is not None:
#     dataframe = pd.read_csv(uploaded_file, index_col=[0])
#     st.write("L'échantillon a bien été chargé !")
#     first_row = dataframe.head(1)

#     payload_test = {}
#     for i, col in enumerate(first_row):
#         payload_test[first_row.columns[i]] = first_row[col][0]


# if uploaded_file is not None:
#     payload_test = {}
#     for i, col in enumerate(first_row):
#         payload_test[first_row.columns[i]] = first_row[col][0]

        # print(payload_test)
        # payload_test[first_row.columns[i]] = [first_row[col][0]]
    # payload_test[first_row.columns[i]].append(value)


# ### get prediction
# url = 'http://127.0.0.1:8000/predict'
# headers = {'content-type': 'application/json'}

# if st.button("send"):
#     send_sample(payload_test, url, headers)

# if st.button("send"):
#     resp = requests.post(url=url, json=payload_test, headers=headers)
#     prediction = resp.text[:5]
#     print(prediction)
#     st.write(f"La prédiction de la résistance à 28 jours pour cet échantillon est de {prediction} MPa")


# uploaded_file = st.file_uploader("Téléverser un fichier csv")

# if uploaded_file is not None:
#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file, index_col=[0])
#     st.write(dataframe)
#     print(type(uploaded_file))

    # url = ' http://127.0.0.1:8000/predict'

    # files = {'file': (dataframe, 'rb')}

    # send_samples(files, url)

# payload = {
#            "echantillon": "text",
#            "elem_ch_1": 0.1,
#            "elem_ch_2": 0.1,
#            "elem_ch_3": 0.1,
#            "elem_ch_4": 0.1,
#            "elem_ch_5": 0.1,
#            "elem_ch_6": 0.1,
#            "elem_ch_7": 0.1,
#            "elem_ch_8": 0.1,
#            "elem_ch_9": 0.1,
#            "elem_ch_10": 0.1,
#            "elem_ch_11": 0.1,
#            "elem_ch_12": 0.1,
#            "elem_ch_13": 0.1,
#            "elem_ch_14": 0.1,
#            "elem_ch_15": 0.1,
#            "elem_ch_16": 0.1,
#            "elem_ch_17": 0.1,
#            "elem_ch_18": 0.1,
#            "elem_ch_19": 0.1,
#            "elem_ch_20": 0.1,
#            "elem_ch_21": 0.1,
#            "elem_ch_22": 0.1,
#            "elem_ch_23": 0.1,
#            "elem_ch_24": 0.1,
#            "elem_ch_25": 0.1,
#            "elem_ch_26": 0.1,
#            "elem_ch_27": 0.1,
#            "elem_ch_28": 0.1,
#            "elem_ch_29": 0.1,
#            "elem_ch_30": 0.1,
#            "elem_ch_31": 0.1,
#            "elem_ch_32": 0.1,
#            "elem_ch_33": 0.1,
#            "elem_ch_34": 0.1,
#            "elem_ch_35": 0.1,
#            "elem_ch_36": 0.1,
#            "elem_ch_37": 0.1,
#            "elem_ch_38": 0.1,
#            "elem_ch_39": 0.1,
#            "elem_ch_40": 0.1,
#            "rc28j_moy": 45.1,
#            "d_0_1": 0.1,
#            "d_0_2": 0.1,
#            "d_0_5": 0.1,
#            "d_0_8": 0.1,
#            "d_0_9": 0.1,
#            "d_3_2": 0.1,
#            "d_4_3": 0.1,
#            "param_rr_1": 0.1,
#            "param_rr_2": 0.1,
#            "param_rr_3": 0.1
#            }