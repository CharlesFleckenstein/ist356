import pandas as pd
import streamlit as st
data = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log',header=3,sep=' ',skiprows=[4])
# also can do skiprows=3 then header=0
timedata = data[data['time-taken'] > 500] 
finaldata = timedata[timedata['sc-status'] == 200]
st.dataframe(finaldata)
slow_ok_filter = (data['time-taken'] > 500) & (log['sc-status'] == 200)
st.dataframe(data[slow_ok_filter])