'''
Web App developed as demo for the "Web Visualization Workshop 2023" at Aalto Geoinformatics Research Lab.
Get familiar with the documentation to get ful capacity of the Web App test.

Author. Bryan R. Vallejo

Data:
    - OpenCell [Ecuador] CC-BY from: https://opencellid.org/downloads.php
    - Bike-sharing system stations [Helsinki] CC-BY from: https://hri.fi/data/en_GB/dataset/hsl-n-kaupunkipyoraasemat

Multiapps connected
    1) Read data , dataframe, and display on Map
    2) Read data, add slider for capacity in bike station, and display map
    3) Create a multipage app
    4) Read data and display heatmap
    5) Read data, subset antenna technology, display heatmap
    6) Add a download button
'''

import streamlit as st
import geopandas as gpd
import pandas as pd 


## ___________________ HELLO APP _______________________ 

st.set_page_config(page_title="Web Visualization Workshop 2023", page_icon="👋", layout="centered", initial_sidebar_state="collapsed")

# title
st.markdown("#### ***Web Visualization Workshop 2023***🧐")


















##END