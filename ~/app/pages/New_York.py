import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of New York")

details = st.selectbox('Check New York city details in the SNAP Program',
                       ('Choose','New York City Map', 'New York potential Gap Rate',
                       'New York SNAP Data', 'New York Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in New York'))


if details == 'New York City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [40.71, -74.00],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'New York potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for New York is N/A")
  
if details == 'New York SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for New York is N/A")
  
    
    
if details == 'New York Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/new_york_povertyline.csv')
  st.markdown("New York SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "New York Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in New York':
  st.write("You are currently viewing: ", details)
  df = 89
  st.write("The % No of people living in New York Eligible for the SNAP Program is \n\n{}%".format(df))
