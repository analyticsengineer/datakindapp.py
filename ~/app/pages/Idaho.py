import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Idaho")

details = st.selectbox('Check Idaho city details in the SNAP Program',
                       ('Choose','Idaho City Map', 'Idaho potential Gap Rate',
                       'Idaho SNAP Data', 'Idaho Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Idaho'))


if details == 'Idaho City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [44.06, -114.74],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Idaho potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 494.63
  hap = 275.89
  st.write("The potential Gap Rate for Idaho city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Idaho city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 494.63], ['Household and Non Household', 275.89]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Idaho SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/idaho.csv')
   st.markdown("Idaho SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Idaho SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Idaho Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/idaho_povertyline.csv')
  st.markdown("Idaho SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Idaho  Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Idaho':
  st.write("You are currently viewing: ", details)
  df = 74
  st.write("The % No of people living in Idaho Eligible for the SNAP Program is \n\n{}%".format(df))
