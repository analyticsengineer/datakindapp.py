import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Florida")

details = st.selectbox('Check Florida city details in the SNAP Program',
                       ('Choose','Florida City Map', 'Florida potential Gap Rate',
                       'Florida SNAP Data', 'Florida Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Florida'))


if details == 'Florida City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [27.66, -81.51],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Florida potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 768.63
  hap = 402.63
  st.write("The potential Gap Rate for Florida city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Florida city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 768.63], ['Household and Non Household', 402.63]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Florida SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/florida.csv')
   st.markdown("Florida SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Florida SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Florida Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/florida_povertyline.csv')
  st.markdown("Florida SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Florida Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Florida':
  st.write("You are currently viewing: ", details)
  df = 86
  st.write("The % No of people living in Florida Eligible for the SNAP Program is \n\n{}%".format(df))
