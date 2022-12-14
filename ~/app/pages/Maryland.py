import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Maryland")

details = st.selectbox('Check Maryland city details in the SNAP Program',
                       ('Choose','Maryland City Map', 'Maryland potential Gap Rate',
                       'Maryland SNAP Data', 'Maryland Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Maryland'))


if details == 'Maryland City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [39.04, -76.64],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Maryland potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for MAryland is N/A")
  
if details == 'Maryland SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for MAryland is N/A")
  
    
    
if details == 'KMaryland Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/maryland_povertyline.csv')
  st.markdown("Maryland SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Maryland Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Maryland':
  st.write("You are currently viewing: ", details)
  df = 91
  st.write("The % No of people living in Maryland Eligible for the SNAP Program is \n\n{}%".format(df))
