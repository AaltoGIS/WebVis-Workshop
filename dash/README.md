# Workshop demo - Plotly App: UK houseprices

- Visualize average England and Wales house prices and sales volume by postcode (sector) from 1995 to 2020
- Show average house price and sales volume trends.
- Show top 500 schools in UK.

Plotly web app ([https://ukhouseprice.project-ds.net/](https://ukhouseprice.project-ds.net/))

![Screenshot](https://github.com/ivanlai/apps-UK_houseprice/blob/master/images/Screenshot-plotly-app.png)

## Credits

This is a Dash app developed by [ivanlai](https://github.com/ivanlai/apps-UK_houseprice)

## Getting started

- Install the conda environment with mamba by running the following from terminal (inside the `dash` -directory):

   ```mamba env create -f environment.yml```

- Activate the environment:

   ```conda activate dashapp```

- Run the app by:

   ```python app.py```

## Where does the magic happen?

Investigate following files:

- [app.py](app.py) -> Contains the visual components (*view*), middleware logic (*controller*)
- [appData](appData/) -> Contains all the data (*model*)
