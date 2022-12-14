import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Kentucky")

details = st.selectbox('Check Kentucky city details in the SNAP Program',
                       ('Choose','Kentucky City Map', 'Kentucky potential Gap Rate',
                       'Kentucky SNAP Data', 'Iowa Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Kentucky'))


if details == 'Kentucky City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.83, -84.27],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Kentucky potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 8350.91
  hap = 9628.40
  st.write("The potential Gap Rate for Kentucky city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Kentucky city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 8350.91], ['Household and Non Household', 9628.40]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Kentucky SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/kentucky.csv')
   st.markdown("Kentucky SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Kentucky SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Kentucky Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/kentucky_povertyline.csv')
  st.markdown("Kentucky SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Kentucky Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Kentucky':
  st.write("You are currently viewing: ", details)
  df = 75
  st.write("The % No of people living in Kentucky Eligible for the SNAP Program is \n\n{}%".format(df))
