import pandas as pd
import numpy as np
import streamlit as st

st.header("City Of Alabama")

details = st.selectbox('Check Arizona city details in the SNAP Program',
                       ('Choose','Arizona City Map', 'Arizona potential Gap Rate',
                       'Arizona SNAP Data', 'Arizona Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Arizona'))


if details == 'Arizona City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [34.04, -111.09],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Arizona potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 4926.64
  hap = 8229.20
  st.write("The potential Gap Rate for Arizona city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Arizona city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  
if details == 'Arizona SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/arizona.csv')
   st.markdown("Arizona SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Arizona SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Arizona Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/arizona_povertyline.csv')
  st.markdown("Arizona SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Arizona Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Arizona':
  st.write("You are currently viewing: ", details)
  df = 77
  st.write("The % No of people living in Arizona Eligible for the SNAP Program is \n\n{}%".format(df))
