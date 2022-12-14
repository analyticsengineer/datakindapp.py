import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Michigan")

details = st.selectbox('Check Michigan city details in the SNAP Program',
                       ('Choose','Michigan City Map', 'Michigan potential Gap Rate',
                       'Michigan SNAP Data', 'Michigan Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Michigan'))


if details == 'Michigan City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [44.31, -85.60],
        columns=['lat', 'lon'])
  st.map(df)
  
if details == 'Michigan potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Michigan is N/A")
  
if details == 'Michigan SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Michigan is N/A")
   
    
    
if details == 'Michigan Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/michigan_povertyline.csv')
  st.markdown("Michigan SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Michigan Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Michigan':
  st.write("You are currently viewing: ", details)
  df = 90
  st.write("The % No of people living in Michigan Eligible for the SNAP Program is \n\n{}%".format(df))
