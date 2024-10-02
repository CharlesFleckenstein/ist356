import pandas as pd
import numpy as np
import streamlit as st
import requests



response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")
employees = response.json()

dataframes = []
for key in employees.keys():
    df = pd.DataFrame(employees[key])
    df['Department'] = key
    dataframes.append(df)

combined_dataframe= pd.concat(dataframes, ignore_index=True)
st.dataframe(combined_dataframe)
    