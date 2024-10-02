import pandas as pd
import streamlit as st
import requests
link = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json'
response = requests.get(link)
data = response.json()
de_data = pd.json_normalize(data, record_path='employees', meta=['dept'])
st.dataframe(de_data)