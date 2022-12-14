import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Indiana")

details = st.selectbox('Check Indiana city details in the SNAP Program',
                       ('Choose','Indiana City Map', 'Indiana potential Gap Rate',
                       'Indiana SNAP Data', 'Indiana Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Indiana'))


if details == 'Indiana City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [40.26, -88.13],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Indiana potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 855.71
  hap = 393.11
  st.write("The potential Gap Rate for Indiana city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Indiana city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 855.71], ['Household and Non Household', 393.11]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Indiana SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/indiana.csv')
   st.markdown("Indiana SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Indiana SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Indiana Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/indiana_povertyline.csv')
  st.markdown("Indiana SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Indiana Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Indiana':
  st.write("You are currently viewing: ", details)
  df = 75
  st.write("The % No of people living in Indiana Eligible for the SNAP Program is \n\n{}%".format(df))
