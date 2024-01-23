
import os
import streamlit as st
import requests
import random
import json

cml_api_key = os.environ["cml_api_key"]
project_name = os.environ["project_name"]
domain = os.getenv("CDSW_DOMAIN")
cml_url = f"https://{domain}"

import cmlapi

client = cmlapi.default_client(url=cml_url, cml_api_key=cml_api_key)
list_of_projects = client.list_projects().__dict__["_projects"]
a = list(filter(lambda p: p.name == project_name, list_of_projects))
project_id = a[0].id
access_key = client.list_models(project_id).models[0].access_key
#main app

#access_key = os.getenv("MODEL_ACCESS_KEY")
prediction_url = f'https://modelservice.{domain}/model'

predictions = st.button("10 random predictions")

pred = []
if predictions:
    for i in range(0,10):
        delay = random.randint(1, 100)
        data = {"accessKey": access_key, "request": {"dep_delay":delay}}
        r = requests.post(prediction_url,
                           data=json.dumps(data), 
                           headers={'Content-Type': 'application/json'})
        pred.append(r.json())


st.write(pred)
