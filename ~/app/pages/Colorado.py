import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Colorado")

details = st.selectbox('Check Colorado city details in the SNAP Program',
                       ('Choose','Colorado City Map', 'Colorado potential Gap Rate',
                       'Colorado SNAP Data', 'Colorado Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Colorado'))


if details == 'Colorado City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [39.55, -105.78],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Colorado potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 1338.24
  hap = 1094.38
  st.write("The potential Gap Rate for Colorado city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Colorado city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 1338.24], ['Household and Non Household', 1094.38]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Colorado SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/colorado.csv')
   st.markdown("Colorado SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Colorado SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Colorado Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/colorado_povertyline.csv')
  st.markdown("Colorado SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Colorado Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Colorado':
  st.write("You are currently viewing: ", details)
  df = 79
  st.write("The % No of people living in Colorado Eligible for the SNAP Program is \n\n{}%".format(df))
