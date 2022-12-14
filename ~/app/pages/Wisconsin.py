import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Wisconsin")

details = st.selectbox('Check Wisconsin city details in the SNAP Program',
                       ('Choose','Wisconsin City Map', 'Wisconsin potential Gap Rate',
                       'Wisconsin SNAP Data', 'Wisconsin Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Wisconsin'))


if details == 'Wisconsin City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [43.78, -88.78],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Wisconsin potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Wisconsin is N/A")
  
if details == 'Wisconsin SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Wisconsin is N/A")
    
    
if details == 'Wisconsin Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/wisconsin_povertyline.csv')
  st.markdown("Wisconsin SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Wisconsin Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Wisconsin':
  st.write("You are currently viewing: ", details)
  df = 92
  st.write("The % No of people living in Wisconsin Eligible for the SNAP Program is \n\n{}%".format(df))
