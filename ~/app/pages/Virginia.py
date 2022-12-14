import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Virginia")

details = st.selectbox('Check Virginia city details in the SNAP Program',
                       ('Choose','Virginia City Map', 'Virginia potential Gap Rate',
                       'Virginia SNAP Data', 'Virginia Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Virginia'))


if details == 'VirginiaCity Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.43, -78.65],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Virginia potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Virginia is N/A")
  
if details == 'Virginia SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Virginia is N/A")
    
if details == 'Virginia Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/virginia_povertyline.csv')
  st.markdown("Virginia SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Virginia Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Virginia':
  st.write("You are currently viewing: ", details)
  df = 72
  st.write("The % No of people living in Virginia Eligible for the SNAP Program is \n\n{}%".format(df))
