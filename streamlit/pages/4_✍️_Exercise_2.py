"""
Exercise 2. 

The dataset is already provided in the repository. Follow the instructions in local development.

Data:
    - OpenCell [Ecuador] CC-BY from: https://opencellid.org/downloads.php

"""
import pandas as pd
import streamlit as st

st.markdown("""
            ### ✍️ ***Subset and download Cellular Antennas***
            
            1. Read with *Pandas* the file `cell-antennas-ec-exercise.csv` from `data` folder.
                - Transform the column `datetime` with `pd.to_datetime()`
                - Create a new column `date` and calculate dates as `[value.date() for value in data.datetime]`
            2. Calculate the min and max `date`
            3. Add a Slider widget for datetime. Check [documentation](https://docs.streamlit.io/library/api-reference/widgets/st.slider)
                - Give it a try and use `st.sidebar.slider()`
                - Define two sides slider with parameter `value=(min_date, max_date)`
            4. Get the new selected range of dates as start and end
            5. Subset the Antennas with the new date range
            6. Display an informative message. e.g. Total antennas
            7. Display a map of new subset
            6. Add a download button of new data. Check [documentation](https://docs.streamlit.io/library/api-reference/widgets/st.download_button)
            
            If you want to make it challenging add a map that shows the spatial density. Check [example](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)            
            Also, add the length of the dataframe in the name of the downloaded file.
            Be aware that you don't need to add `@st.cache` because we want rerun.
            
            ##### **Here a Clue**
            
            
            ```
            def convert_df(df):
                return df.to_csv().encode('utf-8')

            csv = convert_df(data_as_df)

            st.sidebar.download_button(
                label="Download filtered data as csv",
                data = csv,
                file_name = 'my_filtered_data.csv',
                mime='text/csv')
            ```
                         
            ---
            """)


## _____ SOLUTION _____


#END