import pandas as pd
import numpy as np
import streamlit as st

st.write("City Of Alabama")

df = pd.read_csv(r'Alabama.csv')
st.markdown("Alabama SNAP Program records: ")
st.write(df)
