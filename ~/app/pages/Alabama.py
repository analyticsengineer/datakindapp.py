import pandas as pd
import numpy as np
import streamlit as st

st.header("City Of Alabama")

details = st.selectbox('Check Alabama city details in the SNAP Program',
                       'Alabama City Map', 'Alabama potential gap rate',
                       'Alabama SNAP data', 'Alabama Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in Alabama')


if details == 'Alabama City Map':
  st.write("You are currently viewing: ", details)
  
  
if details == 'Alabama potential gap rate':
  st.write("You are currently viewing: ", details)
  
if details == 'Alabama SNAP data':
   st.write("You are currently viewing: ", details)
   df = pd.read_csv(r'Alabama.csv')
   st.markdown("Alabama SNAP Program records: ")
   st.dataframe(df)
    
    
if details == 'Alabama Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  
  
 if details == '% No of the people eligible for the SNAP Program in Alabama':
  st.write("You are currently viewing: ", details)
  df = 79
  st.write("The % No of people living in Alabama Eligible for the SNAP Program is {}%".format(df))
  
  
