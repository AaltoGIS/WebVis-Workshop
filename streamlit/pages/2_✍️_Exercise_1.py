"""
Exercise 1. 

The dataset is already provided in the repository. Follow the instructions in local development.

Data:
    - Bike-sharing system stations [Helsinki] CC-BY from: https://hri.fi/data/en_GB/dataset/hsl-n-kaupunkipyoraasemat

"""

import streamlit as st
import pandas as pd


st.markdown("""
            ### ✍️ ***Subset bike-sharing stations with average***
            
            1. Read with *Pandas* the file `bike-sharing-system-exercise-1.csv` from `data` folder.
            2. Store the average bike capacity using the column `Kapasiteet`
            3. Add a checkbox button with `st.checkbox()`. Check the [Documentation](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
            4. Every time you check the box it will subset the bikes with values higher than the average.
            5. Display a communicative message. e.g. Total bike stations.
            6. Display a map
            
            Be sure that you app is always displaying a map even before you click on the checkbox. 
            if you want to make it challenging add two checkboxes, one to subset higher than average 
            and a second to subset lower than average. 
            
            Add the condition, if two boxes are checked then 
            it displays a message: *"You can only check one"*
            
            **Here a Clue**            
            The way to make understand your code that a checkbox is checked is by using `if st.checkbox():`. 
            
            If you add more checkboxes better name them then it is easier to do logic operations.
            
            ---
            """)


## _____ SOLUTION _____

import pandas as pd
import streamlit as st



#END