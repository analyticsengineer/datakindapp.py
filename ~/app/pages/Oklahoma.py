import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Oklahoma")

details = st.selectbox('Check Oklahoma city details in the SNAP Program',
                       ('Choose','Oklahoma City Map', 'Oklahoma potential Gap Rate',
                       'Oklahoma SNAP Data', 'Oklahoma Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Oklahoma'))


if details == 'Oklahoma City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [35.00, -97.09],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Oklahoma potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Oklahoma is N/A")
  
  
if details == 'Kentucky SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Oklahoma is N/A")
   
    
    
if details == 'Oklahoma Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/oklahoma_povertyline.csv')
  st.markdown("Oklahoma SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Oklahoma Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Oklahoma':
  st.write("You are currently viewing: ", details)
  df = 85
  st.write("The % No of people living in Oklahoma Eligible for the SNAP Program is \n\n{}%".format(df))
