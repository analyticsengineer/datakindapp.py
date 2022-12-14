import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Connecticut")

details = st.selectbox('Check Connecticut city details in the SNAP Program',
                       ('Choose','Connecticut City Map', 'Connecticut potential Gap Rate',
                       'Connecticut SNAP Data', 'Connecticut Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Connecticut'))


if details == 'Connecticut City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [41.60, -73.08],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Connecticut potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 1270.41
  hap = 1391.84
  st.write("The potential Gap Rate for Connecticut city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Connecticut city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 1270.41], ['Household and Non Household', 1391.84]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Connecticut SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/connecticut.csv')
   st.markdown("Connecticut SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Connecticut SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Connecticut Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/connecticut_povertyline.csv')
  st.markdown("Connecticut SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Connecticut Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Connecticut':
  st.write("You are currently viewing: ", details)
  df = 93
  st.write("The % No of people living in Connecticut Eligible for the SNAP Program is \n\n{}%".format(df))
