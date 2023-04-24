"""
Exercise 1. 

The dataset is already provided in the repository. Follow the instructions in local development.

Data:
    - Bike-sharing system stations [Helsinki] CC-BY from: https://hri.fi/data/en_GB/dataset/hsl-n-kaupunkipyoraasemat

"""
import pandas as pd
import streamlit as st

st.markdown("""
            ### ✍️ ***Subset bike-sharing stations with average***
            
            1. Read with *Pandas* the file `bike-sharing-system-exercise-1.csv` from `data` folder.
            2. Calculate the average bike capacity using the column `Kapasiteet`
            3. Add a radio button with `st.radio()`. Check the [Documentation](https://docs.streamlit.io/library/api-reference/widgets/st.radio)
            4. Include two options in radio button: 
                - First one to subset values higher than average, 
                - Second one to subset values lower than average
            5. Display a communicative message every time for subset. e.g. Total bike stations.
            6. Display a map
            
            Be sure that you app is always displaying a map even before you click on the radio button. 
            Also, add a third option that says `None` and it display all data with no subset.
                        
            ##### **Here a Clue**
            
            First store your radio button function in a variable once you have added the options like:
            
            `my_options = st.radio()`
            
            Then, the way to make understand your code that a radio button is checked is by using:
            
            `if my_options=='my_selection':`
                                 
            ---
            """)


## _____ SOLUTION _____



#END