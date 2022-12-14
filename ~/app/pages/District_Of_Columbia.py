import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("City Of District Of Columbia")

details = st.selectbox('Check District Of Columbia city details in the SNAP Program',
                       ('Choose','District Of Columbia City Map', 'District Of Columbia potential Gap Rate',
                       'District Of Columbia SNAP Data', 'District Of Columbia Counties below federal poverty line',
                       '% No of the people eligible for the SNAP Program in District Of Columbia'))


if details == 'District Of Columbia City Map':
  st.write("You are currently viewing: ", details)
  df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [38.90, -77.03],
        columns=['lat', 'lon'])
  st.map(df)
  
  
if details == 'District Of Columbia potential Gap Rate':
  st.write("You are currently viewing: ", details)
  st.write("District Of Columbia SNAP DATA IS N/A")
  
if details == 'District Of Columbia SNAP Data':
   st.write("You are currently viewing: ", details)
   st.write("District Of Columbia SNAP DATA IS N/A")
    
    
if details == 'District Of Columbia Counties below federal poverty line':
  st.write("You are currently viewing: ", details)
  df = pd.read_csv(r'Data/doc_povertyline.csv')
  st.markdown("District Of Columbia SNAP Program records: ")
  st.dataframe(df)
  df = pd.DataFrame(df)
  file_name = "District Of Columbia Counties.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
    
  
  
if details == '% No of the people eligible for the SNAP Program in District Of Columbia':
  st.write("You are currently viewing: ", details)
  df = 82
  st.write("The % No of people living in District Of Columbia Eligible for the SNAP Program is \n\n{}%".format(df))
