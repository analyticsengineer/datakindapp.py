import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Missouri")

details = st.selectbox('Check Missouri city details in the SNAP Program',
                       ('Choose','Missouri City Map', 'Missouri potential Gap Rate',
                       'Missouri SNAP Data', 'Missouri Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Missouri'))


if details == 'Missouri City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.96, -91.83],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Missouri potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Missouri is N/A")
  
if details == 'Missouri SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Missouri is N/A")
   
    
    
if details == 'Missouri Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/missouri_povertyline.csv')
  st.markdown("Missouri SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Missouri Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Missouri':
  st.write("You are currently viewing: ", details)
  df = 87
  st.write("The % No of people living in Missouri Eligible for the SNAP Program is \n\n{}%".format(df))
