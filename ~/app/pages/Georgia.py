import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of Georgia")

details = st.selectbox('Check Georgia city details in the SNAP Program',
                       ('Choose','Georgia City Map', 'Georgia potential Gap Rate',
                       'Georgia SNAP Data', 'Georgia Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Georgia'))


if details == 'Georgia City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [32.16, -82.90],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'Georgia potential Gap Rate':
  st.write("You are currently viewing: ", details)
  pap = 740.76
  hap = 531.02
  st.write("The potential Gap Rate for Georgia city Public and Non Public Assistance Participation is \n\n{}". format(pap))
  st.write("The potential Gap Rate for Georgia city Household and Non Household Assistance Participation is \n\n{}". format(hap))
  snap = [['Public and Non Public', 740.76], ['Household and Non Household', 531.02]]
  snap_df = pd.DataFrame(snap, columns=['Assistance Participation', 'Potential Gap Rate'])
  fig = px.bar(snap_df, x=snap_df['Assistance Participation'], y=snap_df['Potential Gap Rate'],  color=snap_df['Assistance Participation'])
  st.plotly_chart(fig, use_container_width=True)
  
if details == 'Georgia SNAP Data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/georgia.csv')
   st.markdown("Georgia SNAP Program records: ")
   st.dataframe(df)
   df = pd.DataFrame(df)
   file_name = "Georgia SNAP Data.csv"
   file_path = f"./{file_name}"

   df.to_csv(file_path)

   df = open(file_path, 'rb')
   st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
   df.close()
    
    
if details == 'Georgia Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/georgia_povertyline.csv')
  st.markdown("Georgia SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "Georgia Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in Georgia':
  st.write("You are currently viewing: ", details)
  df = 84
  st.write("The % No of people living in Georgia Eligible for the SNAP Program is \n\n{}%".format(df))
