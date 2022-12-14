import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Utah")

details = st.selectbox('Check Utah city details in the SNAP Program',
                       ('Choose','Utah City Map', 'Utah potential Gap Rate',
                       'Utah SNAP Data', 'Utah Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Utah'))


if details == 'Utah City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [39.32, -111.09],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Utah potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Utah is N/A")
  
  
if details == 'Utah SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Utah is N/A")
   
    
if details == 'Utah Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/utah_povertyline.csv')
  st.markdown("Utah SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Utah Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Utah':
  st.write("You are currently viewing: ", details)
  df = 77
  st.write("The % No of people living in Utah Eligible for the SNAP Program is \n\n{}%".format(df))
