import pandas as pd
import streamlit as st 
import plotly.express as px
from datetime import datetime
import pydeck as pdk

# page
st.set_page_config(page_title="Cellular Antenna EC", 
                   layout="wide", 
                   initial_sidebar_state="expanded")

## __________ CELLULAR ANTENNA APP _______________ 

st.markdown("""
            ### 📡 ***Cellular Antennas in EC***
            
            Streamlit can be used as a dashboarding tool. You are able to display 
            interactive charts from Plotly, as an example, that help users to interact 
            with the values and understand better the patterns of the data.
            
            We are going to give a view to the Cellular Antennas development in Ecuador 
            with a plotly histogram.
            
            """)

# read cellular antennas
antennas = pd.read_csv('data/OpenCell_EC.csv', sep=';')

# get datetime from UNIX
antennas['datetime'] = [datetime.fromtimestamp(value) for value in antennas['created']]
antennas = antennas.sort_values('datetime', ascending=False)

st.info(f'There in total {len(antennas)} cellular antennas')

## ___________ PLOT _____________ 

# get histogram
fig = px.histogram(antennas, x='datetime')
st.plotly_chart(fig, use_container_width=True)

with st.expander('Code', expanded=False):
    
    st.code("""
            import plotly.express as px

            fig = px.histogram(antennas, x='datetime')
            st.plotly_chart(fig, use_container_width=True)
            
            """)

## _______________ SPATIA DENSITY MAP ________________ 

st.markdown("""
            ### Spatial Density of Antennas
            
            Simple charts like histograms can help to understand the frequency over time 
            but we are interested to know also the frequency in the space. The spatial density 
            gives a visual understanding of where patterns occur.
            
            Take a look the next map showing spatial density.
            
            """)

## ____ HEX LAYER ______ 

st.pydeck_chart(pdk.Deck(
                        map_style=None,
                        initial_view_state=pdk.ViewState(
                                                    latitude=-2.5,
                                                    longitude=-79,
                                                    zoom=6.5,
                                                    pitch=45,
                                                        ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=antennas,
           get_position='[lon, lat]',
           radius=5000,
           elevation_scale=20,
           elevation_range=[0, 5000],
           pickable=True,
           extruded=True,
           coverage=1
                )
            ],
))

with st.expander('Code', expanded=False):
    
    st.code("""            
    import pydeck as pdk
    import streamlit as st
        
    st.pydeck_chart(pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                                                latitude=-2.5,
                                                longitude=-79,
                                                zoom=6.5,
                                                pitch=45,
                                                    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=antennas,
            get_position='[lon, lat]',
            radius=5000,
            elevation_scale=20,
            elevation_range=[0, 5000],
            pickable=True,
            extruded=True,
            coverage=1
                )
            ],
    ))
            
            """)
    
    