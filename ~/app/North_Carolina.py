import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of North Carolina")

details = st.selectbox('Check North Carolina city details in the SNAP Program',
                       ('Choose','North Carolina City Map', 'North Carolina potential Gap Rate',
                       'North Carolina SNAP Data', 'North Carolina Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in North Carolina'))


if details == 'North Carolina City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [35.75, -79.01],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'North Carolina potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for North Carolina is N/A")
  
if details == 'North Carolina SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for North Carolina is N/A")
   
    
    
if details == 'North Carolina Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/north_carolina_povertyline.csv')
  st.markdown("North Carolina SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "North Carolina Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in North Carolina':
  st.write("You are currently viewing: ", details)
  df = 69
  st.write("The % No of people living in North Carolina Eligible for the SNAP Program is \n\n{}%".format(df))
