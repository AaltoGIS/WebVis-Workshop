import streamlit as st
import geopandas as gpd
import pandas as pd 
import pydeck as pdk
import numpy as np

## _____________ HELSINKI BIKES APP __________________ 

# page
st.set_page_config(page_title="Bike-sharing system stations Helsinki", 
                   layout="wide", 
                   initial_sidebar_state="expanded")

## _________________ TABS ________________
tab1, tab2, tab3 = st.tabs(['Statistics', 'Visualization', 'Subset'])

with tab1:
    st.markdown("""
                ### 🚴‍♂️***Helsinki Bike-Sharing System Stations***
                
                The code in the backend is reading the *Bike stations* layer and sotre it in a variable.
                You can calculate frequencies or statistics of your data and call them 
                to the frontend as an informative message.
                
                For example, frequencies or statistics like:
                
                """)

    ## _____________ FREQUENCIES AND STATISTICS __________________ 

    # read data
    bikes = gpd.read_file('data/bike-sharing-system-stations.gpkg')

    # create DataFrame
    bikes_df = bikes[['Name', 'x', 'y', 'Kapasiteet']].rename(columns={'x': 'longitude', 'y':'latitude'})
    bikes_df = pd.DataFrame(bikes_df)

    # frequencies and stats
    count = bikes_df.Name.nunique()

    min = bikes_df.Kapasiteet.min()
    max = bikes_df.Kapasiteet.max()

    avg = round(bikes_df.Kapasiteet.mean(), 2)
    med = round(bikes_df.Kapasiteet.median(), 2)
    std = round(bikes_df.Kapasiteet.std(), 2)
    diff = round(avg-med, 2)

    ## _____________ DISPLAY VALUES __________________ 

    st.success(f'You have read successfully {count} Locations of bike stations at Helsinki-Finland')

    col1, col2 =  st.columns(2)

    with col1:
        st.info(f'The minimum bike capacity is {min} from station {bikes_df.loc[bikes_df.Kapasiteet==min].Name.unique()[0]}')

        st.metric('Average Capacity', value=avg, delta=f'{std} std')
        
    with col2:
        st.error(f'The maximum bike capacity is {max} from station {bikes_df.loc[bikes_df.Kapasiteet==max].Name.unique()[0]}')

        st.metric('Median Capacity', value=med, delta=f'{diff} diff', delta_color='inverse')

    
    with st.expander('Functions used', expanded=False):
        st.code("""
                    st.markdown()
                    
                    ---------------------------------------------------

                    column1, column2 = st.columns(2)
                    
                    with column1:
                        st.info("The minimum bike capacity...")
                        
                    with column2:
                        st.info("The maximum bike capacity...")
                        
                    ---------------------------------------------------
                    
                    st.metric('Label', value = statistic, delta = rate)
                """)
        
## -------------------------------------------------------------------------------------------------

with tab2:
    
    ## _____________ MAP __________________ 

    st.markdown("""              
                ### ***Simple maps with PyDeckGl***
                
                If you have a dataset with ***longitude*** and ***latitude*** you can create
                a simple map with DeckGl. This function is already implemented in Streamlit 
                and supports a quick visualization. Of course, you can create more elaborated 
                maps but you have to create your own object and display it.
                
                Check out the next interactive examples:
                
                """)

    # options
    layers = ['Simple Scatter Map', 'Elaborated Scatter Map']

    # add box
    layer_type = st.selectbox('Choose the kind of visualization you want to display', options=layers, index=0)

    # conditional for layers
    if layer_type==layers[0]:
                
        # map
        st.map(bikes_df, zoom=10)

        with st.expander('Code:', expanded=False):
            st.code("""
                    import streamlit as st
                    
                    st.map(bikes_df, zoom=10)""")
            
    if layer_type==layers[1]:
        
        #map
        st.pydeck_chart(pdk.Deck(
                            map_style='mapbox://styles/mapbox/light-v9',
                            tooltip={"text": "{Name}: {Kapasiteet} Bikes"},
                            
                initial_view_state=pdk.ViewState(
                                                latitude=60.171358,
                                                longitude=24.941349,
                                                zoom=11,
                                                pitch=45,
                                                ),
                layers=[
                        pdk.Layer('ScatterplotLayer',
                                data=bikes_df,
                                pickable=True,
                                opacity=0.6,
                                stroked=True,
                                get_position='[longitude, latitude]',
                                get_color=[18, 84, 199],
                                get_line_color=[0, 0, 0],
                                line_width_min_pixels=1.5,
                                get_radius='Kapasiteet',
                                radius_scale=8,
                                radius_min_pixels=1,
                                radius_max_pixels=100)
                        ],
                    ))
        
        with st.expander('Code:', expanded=False):
        
            st.code("""
                    
                import pydeck as pdk
                import streamlit as st
                
                st.pydeck_chart(pdk.Deck(
                            map_style='mapbox://styles/mapbox/light-v9',
                            tooltip={"text": "{Name}: {Kapasiteet} Bikes"},
                            
                initial_view_state=pdk.ViewState(
                                                latitude=60.171358,
                                                longitude=24.941349,
                                                zoom=11,
                                                pitch=45,
                                                ),
                layers=[
                        pdk.Layer('ScatterplotLayer',
                                data=bikes_df,
                                pickable=True,
                                opacity=0.6,
                                stroked=True,
                                get_position='[longitude, latitude]',
                                get_color=[18, 84, 199],
                                get_line_color=[0, 0, 0],
                                line_width_min_pixels=1.5,
                                get_radius='Kapasiteet',
                                radius_scale=8,
                                radius_min_pixels=1,
                                radius_max_pixels=100)
                        ],
                    ))
                """)
            
## -------------------------------------------------------------------------------------------------

with tab3:
    
    st.markdown("""
                ### ***Filtering data with UI***
                
                The User Interaction(UI) can be used as a ***input variables*** for creating new subsets of data.
                The main step is that you define the attributes you want to use for subseting data and add 
                them as options in the UI. It can be names or values, depends on your need you might find 
                the right Streamlit function.
                
                Let's check some examples with the Bike-sharing data in Helsinki.
                

                ###### *1) Let's define the limits of the bike capacity in two Float variables*

                ###### *2) Define the Slider with bike capacity*
                
                ###### *3) Subset the range*
                
                ###### *4) Map the subset*
                
                """)
    
    with st.expander('Check the code', expanded=False):
        
        st.code("""
                # 1 define range of float variables to subset
                min_capacity = float(bikes_df.Kapasiteet.min())
                max_capacity = float(bikes_df.Kapasiteet.max())
                
                # 2 define slider
                range = st.slider('Choose the bike capacity range', 
                                    min_value=min_capacity, 
                                    max_value=max_capacity, 
                                    value=(min_capacity, max_capacity),
                                    step = 1.0)
                
                # 3 subset data
                min, max = range                
                subset = bikes_df.loc[(bikes_df.Kapasiteet>=min) & (bikes_df.Kapasiteet<=max)]
                
                # 4 map
                st.map(subset, zoom=10)
                """)
        
    st.markdown("""---""")
    
    # define range of variables to subset
    min_capacity = float(bikes_df.Kapasiteet.min())
    max_capacity = float(bikes_df.Kapasiteet.max())
    
    st.write(f"""
                The minimum bike capacity is **{min_capacity}** and the maximum is **{max_capacity}**. 
                Both values are used as limits in the slider.
                
                """)

    # define slider
    range = st.slider('Choose the bike capacity range', 
                min_value=min_capacity, 
                max_value=max_capacity, 
                value=(min_capacity, max_capacity),
                step = 1.0)
    
    st.write('Range selected:', range)
    
    # subset data
    min, max = range
    
    subset = bikes_df.loc[(bikes_df.Kapasiteet>=min) & (bikes_df.Kapasiteet<=max)]
    
    #map
    st.map(subset, zoom=10)
    
    # table
    subset = subset.sort_values('Kapasiteet', ascending=False).reset_index(drop=True)
    
    st.dataframe(subset)
        