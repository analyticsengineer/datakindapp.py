import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


# App Header
col1, col2 = st.columns(2)
image = Image.open('image.png')


col1.image(image)

col1.write("This Web application consists of only states with counties below federal poverty line")

col1.write("[![Project Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/anuoluwapods/datakindapp.py)")



