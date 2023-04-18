'''
Web App developed as demo for the "Web Visualization Workshop 2023" at Aalto Geoinformatics Research Lab.
Get familiar with the documentation to get ful capacity of the Web App test.

Author. Bryan R. Vallejo

Data:
    - OpenCell [Ecuador] CC-BY from: https://opencellid.org/downloads.php
    - Bike-sharing system stations [Helsinki] CC-BY from: https://hri.fi/data/en_GB/dataset/hsl-n-kaupunkipyoraasemat

Scenarios
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


## ___________________ SCENE 1 _______________________ 

# read data
bikes = gpd.read_file('data/bike-sharing-system-stations.gpkg')

# count unique bike stations
count = bikes.Name.nunique()

st.success(f'You have read successfully {count} Locations of bike stations at Helsinki-Finland')

# create DataFrame
bikes_df = bikes[['Name', 'x', 'y']].rename(columns={'x': 'longitude', 'y':'latitude'})
bikes_df = pd.DataFrame(bikes_df)

# map
st.map(bikes_df, zoom=10)

st.write(bikes_df)
# st.map(bikes)

## ___________________ SCENE 2 _______________________ 

## ___________________ SCENE 3 _______________________ 

## ___________________ SCENE 4 _______________________ 

## ___________________ SCENE 5 _______________________ 

## ___________________ SCENE 6 _______________________ 



















##END