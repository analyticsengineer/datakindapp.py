import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Iowa")

details = st.selectbox('Check Iowa city details in the SNAP Program',
                       ('Choose','Iowa City Map', 'Iowa potential Gap Rate',
                       'Iowa SNAP Data', 'Iowa Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Iowa'))


if details == 'Iowa City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [41.87, -93.09],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Iowa potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 564.46
  hap = 320.10
  st.write("The potential Gap Rate for Florida city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Florida city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 564.46], ['Household and Non Household', 320.10]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Iowa SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/iowa.csv')
   st.markdown("Iowa SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Iowa SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Iowa Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/iowa_povertyline.csv')
  st.markdown("Iowa SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Iowa Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Iowa':
  st.write("You are currently viewing: ", details)
  df = 89
  st.write("The % No of people living in Iowa Eligible for the SNAP Program is \n\n{}%".format(df))
