import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Illinois")

details = st.selectbox('Check Illinois city details in the SNAP Program',
                       ('Choose','Illinois City Map', 'Illinois potential Gap Rate',
                       'Illinois SNAP Data', 'Illinois Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Illinois'))


if details == 'Illinois City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [40.63, -89.39],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Illinois potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 2800.67
  hap = 4626.52
  st.write("The potential Gap Rate for Illinois city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Illinois city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 2800.67], ['Household and Non Household', 4626.52]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Illinois SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/illinois.csv')
   st.markdown("Illinois SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Illinois SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Illinois Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/illinois_povertyline.csv')
  st.markdown("Illinois SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Illinois Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Illinois':
  st.write("You are currently viewing: ", details)
  df = 100
  st.write("The % No of people living in Illinois Eligible for the SNAP Program is \n\n{}%".format(df))
