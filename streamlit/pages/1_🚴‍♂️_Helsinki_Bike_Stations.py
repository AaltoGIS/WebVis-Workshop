import streamlit as st
import geopandas as gpd
import pandas as pd 



## _____________ HELSINKI BIKES APP __________________ 

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
