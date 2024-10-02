import pandas as pd
import numpy as np
import streamlit as st
import requests

base = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/'
customers = pd.read_csv(base + '/customers.csv')
months = ['jan', 'feb', 'mar','apr']
month_df = []
for month in months:
    month_dff = pd.read_csv(base + f'/purchases-{month}.csv')
    month_dff['month']= month
    month_df.append(month_dff)
purchases= pd.concat(month_df, ignore_index=True)
filt_df = pd.merge(purchases, customers, on='customer_id', how='left')
no_purchase = filt_df[filt_df['order_id'].isna()]

st.dataframe(no_purchase)