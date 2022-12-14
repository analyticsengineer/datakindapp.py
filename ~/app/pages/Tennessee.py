import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Tennessee")

details = st.selectbox('Check Tennessee city details in the SNAP Program',
                       ('Choose','Tennessee City Map', 'Tennessee potential Gap Rate',
                       'Tennessee SNAP Data', 'Tennessee Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Tennessee'))


if details == 'Tennessee City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [35.51, -86.58],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Tennessee potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Tennessee is N/A")
  
if details == 'Tennessee SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Tennessee is N/A")
    
    
if details == 'Tennessee Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/tennessee_povertyline.csv')
  st.markdown("Tennessee SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Tennessee Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Tennessee:
  st.write("You are currently viewing: ", details)
  df = 90
  st.write("The % No of people living in Tennessee Eligible for the SNAP Program is \n\n{}%".format(df))
