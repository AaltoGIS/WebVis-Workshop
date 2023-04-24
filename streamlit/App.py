'''
Web App developed as demo for the "Web Visualization Workshop 2023" at Aalto Geoinformatics Research Lab.
Get familiar with the documentation to get ful capacity of the Web App test.

Author. Bryan R. Vallejo

Data:
    - OpenCell [Ecuador] CC-BY from: https://opencellid.org/downloads.php
    - Bike-sharing system stations [Helsinki] CC-BY from: https://hri.fi/data/en_GB/dataset/hsl-n-kaupunkipyoraasemat

Multiapps connected
    1) Helsinki bike-sharing system
        - Statistics:       columns, messages, metrics
        - Visualization:    map layers
        - Subset:           slider
'''

import streamlit as st
import geopandas as gpd
import pandas as pd 


## ___________________ APP _______________________ 

st.set_page_config(page_title="Web Visualization Workshop 2023", 
                   page_icon="👋", 
                   layout="centered", 
                   initial_sidebar_state="collapsed")

# info
st.markdown("""
            ## ***Web Visualization Workshop 2023***🧐
            
        This web app was developed to showcase the capabilities of Streamlit
        as a User Interactive (UI) framework for scientific communication. 
        
        ###### 👈 ***Select a Demo from the sidebar to undertand the capabilities of Streamlit***
        
        #### Datasets
        - [**Helsinki Bike-sharing System Stations**](https://hri.fi/data/en_GB/dataset/hsl-n-kaupunkipyoraasemat)
    
            *Helsinki Region Transport's (HSL) city bicycle stations. The maintainer of the dataset 
            is Helsingin seudun liikenne HSL. The dataset has been downloaded from Helsinki Region 
            Infoshare service on 20.04.2023 under the license Creative Commons Attribution 4.0.*
            
        - [**OpenCellID Antennas Locations in Ecuador**](https://opencellid.org/downloads.php)

            *OpenCelliD Project is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License*
            
        #### Code Repository
        - [**Web Visualization Code Repository**](https://github.com/AaltoGIS/WebVis-Workshop)
        
            *Geoinformatics Department at Aalto University (2023). Licensed under CC-BY.*
            
        #### Useful links
        - [**Google Earth Engine in Streamlit**](https://towardsdatascience.com/monitoring-sea-surface-temperature-at-the-global-level-with-gee-1d7349c7da6?sk=ad86cafc4621810ca75020b830588287)
            
            *Monitoring Sea Surface Temperature at the global level with GEE. How to create a Streamlit app for ocean monitoring with Python. By B. R. Vallejo*
        
        - [**Satellite Imagery Timelapse in Streamlit**](https://huggingface.co/spaces/giswqs/Streamlit)
        
        *An interactive web app for creating Landsat/GOES timelapse for any location around the globe. The app was built using streamlit, geemap, and Google Earth Engine. By Q. Wu.
        
            """)

















##END