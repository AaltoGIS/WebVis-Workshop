# main app
import streamlit as st
import geopandas as gpd
import plotly.express as px

st.set_page_config(page_title="My Page", layout="wide")

st.title('Hello World')

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

fig = px.scatter_mapbox(geo_df,
                        lat=geo_df.geometry.y,
                        lon=geo_df.geometry.x,
                        hover_name="name",
                        mapbox_style='carto-positron',
                        height=700,
                        zoom=2)

st.plotly_chart(fig, use_container_width=True)
