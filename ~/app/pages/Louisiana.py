import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Louisiana")

details = st.selectbox('Check Louisiana city details in the SNAP Program',
                       ('Choose','Louisiana City Map', 'Louisiana potential Gap Rate',
                       'Louisiana SNAP Data', 'Louisiana Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Louisiana'))


if details == 'Louisiana City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [30.98, -91.96],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Louisiana potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("The SNAP DATA for Louisiana is N/A")
  
if details == 'Louisiana SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("The SNAP DATA for Louisiana is N/A")
    
    
if details == 'Louisiana Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/louisiana_povertyline.csv')
  st.markdown("Louisiana SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Louisiana Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Louisiana':
  st.write("You are currently viewing: ", details)
  df = 83
  st.write("The % No of people living in Louisiana Eligible for the SNAP Program is \n\n{}%".format(df))
