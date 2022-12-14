import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Nevada")

details = st.selectbox('Check Nevada city details in the SNAP Program',
                       ('Choose','Nevada City Map', 'Nevada potential Gap Rate',
                       'Nevada SNAP Data', 'Nevada Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Nevada'))


if details == 'Nevada City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [38.80, -116.41],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Nevada potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Nevada is N/A")
  
if details == 'Nevada SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Nevada is N/A")
   
    
if details == 'Nevada Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/nevada_povertyline.csv')
  st.markdown("Nevada SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Nevada Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Nevada':
  st.write("You are currently viewing: ", details)
  df = 92
  st.write("The % No of people living in Nevada Eligible for the SNAP Program is \n\n{}%".format(df))
