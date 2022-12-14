import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Ohio")


details = st.selectbox('Check Ohio city details in the SNAP Program',
                       ('Choose','Ohio City Map', 'Ohio potential Gap Rate',
                       'Ohio SNAP Data', 'Ohio Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Ohio'))


if details == 'Ohio City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [40.41, -82.90],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Ohio potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Ohio is N/A")
  
if details == 'Ohio SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Ohio is N/A")
   
    
    
if details == 'Ohio Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/ohio_povertyline.csv')
  st.markdown("Ohio SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Ohio Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Ohio':
  st.write("You are currently viewing: ", details)
  df = 85
  st.write("The % No of people living in Ohio Eligible for the SNAP Program is \n\n{}%".format(df))
