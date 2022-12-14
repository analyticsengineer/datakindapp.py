import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of California")

details = st.selectbox('Check California city details in the SNAP Program',
                       ('Choose','California City Map', 'California potential Gap Rate',
                       'California SNAP Data', 'California Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in California'))


if details == 'California City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [36.78, -119.41],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'California potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 242.60
  hap = 187.36
  st.write("The potential Gap Rate for California city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for California city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public Assistance Participation', 242.60], ['Household and Non Household Assistance Participation', 187.36]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'California SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/california.csv')
   st.markdown("California SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "California SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'California Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/california_povertyline.csv')
  st.markdown("California SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "California Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in California':
  st.write("You are currently viewing: ", details)
  df = 70
  st.write("The % No of people living in California Eligible for the SNAP Program is \n\n{}%".format(df))
