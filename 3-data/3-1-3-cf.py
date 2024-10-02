import streamlit as st
import certifi
import pandas as pd
import numpy as np

link = 'https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv'
link ='customers.csv'
customers = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')

choice = st.radio('Select gender', ["m","f"])
cols = st.multiselect('Select columns', customers.columns)
gender_index = customers['Gender'] ==choice

st.dataframe(customers[gender_index][cols])