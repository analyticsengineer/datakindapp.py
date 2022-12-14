import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Minnesota")

details = st.selectbox('Check Minnesota city details in the SNAP Program',
                       ('Choose','Minnesota City Map', 'Minnesota potential Gap Rate',
                       'Minnesota SNAP Data', 'Minnesota Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Minnesota'))


if details == 'Minnesota City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [46.72, -94.68],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Minnesota potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Minnesota is N/A")
  
if details == 'Minnesota SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Minnesota is N/A")
   
    
    
if details == 'Minnesota Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/minnesota_povertyline.csv')
  st.markdown("Minnesota SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Minnesota Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Minnesota':
  st.write("You are currently viewing: ", details)
  df = 77
  st.write("The % No of people living in Minnesota Eligible for the SNAP Program is \n\n{}%".format(df))
