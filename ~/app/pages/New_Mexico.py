import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of New Mexico")

details = st.selectbox('Check New Mexico city details in the SNAP Program',
                       ('Choose','New Mexico City Map', 'New Mexico potential Gap Rate',
                       'New Mexico SNAP Data', 'New Mexico Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in New Mexico'))


if details == 'New Mexico City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [34.51, -105.87],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'New Mexico potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for New Mexico is N/A")
  
if details == 'New Mexico SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for New Mexico is N/A")
   
    
if details == 'New Mexico Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/new_mexico_povertyline.csv')
  st.markdown("New Mexico SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "New Mexico Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in New Mexico':
  st.write("You are currently viewing: ", details)
  df = 98
  st.write("The % No of people living in New Mexico Eligible for the SNAP Program is \n\n{}%".format(df))
