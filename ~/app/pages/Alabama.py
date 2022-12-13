import pandas as pd
import numpy as np
import streamlit as st

st.header("City Of Alabama")

details = st.selectbox('Check Alabama city details in the SNAP Program',
                       ('Alabama City Map', 'Alabama potential gap rate',
                       'Alabama SNAP data', 'Alabama Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Alabama'))


if details == 'Alabama City Map':
  st.write("You are currently viewing: ", details)
  df1 = pd.DataFrame(
                 np.random.randn(1000, 2) / [50, 50] + [32.32, -86.9],
                 columns=['lat', 'lon'])
  st.map(df1)
  
  
if details == 'Alabama potential gap rate':
  st.write("You are currently viewing: ", details)
  
if details == 'Alabama SNAP data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Data/alabama.csv')
   st.markdown("Alabama SNAP Program records: ")
   st.dataframe(df)
   def convert_df(df):
      return df.to_csv().encode('utf-8')
      csv = convert_df(df)
      st.download_button(
      label="Download data as CSV",
      data=csv,
      file_name='Alabama City Snap Data.csv',
      mime='text/csv',
      )
    
    
if details == 'Alabama Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  
  
if details == '% No of the people eligible for the SNAP Program in Alabama':
  st.write("You are currently viewing: ", details)
  df = 79
  st.write("The % No of people living in Alabama Eligible for the SNAP Program is {}%".format(df))
  
  
