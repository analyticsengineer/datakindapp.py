import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of South Carolina")

details = st.selectbox('Check South Carolina city details in the SNAP Program',
                       ('Choose','South Carolina City Map', 'South Carolina potential Gap Rate',
                       'South Carolina SNAP Data', 'South Carolina Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in South Carolina'))


if details == 'South Carolina City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [33.83, -81.16],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'South Carolina potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for South Carolina is N/A")
  
if details == 'South Carolina SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for South Carolina is N/A")
    
    
if details == 'South Carolina Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/south_carolina_povertyline.csv')
  st.markdown("South Carolina SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "South Carolina Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in South Carolina':
  st.write("You are currently viewing: ", details)
  df = 77
  st.write("The % No of people living in South Carolina Eligible for the SNAP Program is \n\n{}%".format(df))
