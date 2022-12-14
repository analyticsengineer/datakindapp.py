import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Pennsylvania")

details = st.selectbox('Check Pennsylvania city details in the SNAP Program',
                       ('Choose','Pennsylvania City Map', 'Pennsylvania potential Gap Rate',
                       'Pennsylvania SNAP Data', 'Pennsylvania Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Pennsylvania'))


if details == 'Pennsylvania City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [41.20, -77.19],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Pennsylvania potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Pennsylvania is N/A")
  
if details == 'Pennsylvania SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Pennsylvania is N/A")
    
if details == 'Pennsylvania Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/pennsylvania_povertyline.csv')
  st.markdown("Pennsylvania SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Pennsylvania Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Pennsylvania':
  st.write("You are currently viewing: ", details)
  df = 100
  st.write("The % No of people living in Pennsylvania Eligible for the SNAP Program is \n\n{}%".format(df))
