import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Texas")

details = st.selectbox('Check Texas city details in the SNAP Program',
                       ('Choose','Texas City Map', 'Texas potential Gap Rate',
                       'Texas SNAP Data', 'Texas Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Texas'))


if details == 'Texas City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [31.96, -99.90],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Texas potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Texas is N/A")
  
if details == 'Texas SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Texas is N/A")
   
    
    
if details == 'Texas Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/texas_povertyline.csv')
  st.markdown("Texas SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Texas Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Texas':
  st.write("You are currently viewing: ", details)
  df = 75
  st.write("The % No of people living in Texas Eligible for the SNAP Program is \n\n{}%".format(df))
