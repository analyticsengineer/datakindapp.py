import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Alabama")

details = st.selectbox('Check Alabama city details in the SNAP Program',
                       ('Choose','Alabama City Map', 'Alabama potential Gap Rate',
                       'Alabama SNAP Data', 'Alabama Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Alabama'))


if details == 'Alabama City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [32.31, -86.90],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Alabama potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 375.94
  hap = 368.16
  st.write("The potential Gap Rate for Alabama city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Alabama city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 375.94], ['Household and Non Household', 368.16]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
  
if details == 'Alabama SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/alabama.csv')
   st.markdown("Alabama SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Alabama SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Alabama Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/alabama_povertyline.csv')
  st.markdown("Alabama SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Alabama Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Alabama':
  st.write("You are currently viewing: ", details)
  df = 79
  st.write("The % No of people living in Alabama Eligible for the SNAP Program is \n\n{}%".format(df))
  
  
