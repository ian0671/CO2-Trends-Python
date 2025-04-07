# Author: Ian Knightly
# Date: 2025-04-04
# Version: 1.0
# License: MIT License
# description:
# This script fetches the Mauna Loa CO2 annual mean growth rate data from NOAA, processes it, and handles missing values.

import pandas as pd
import requests
from io import StringIO

url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_mlo.txt"
response = requests.get(url)

if response.status_code == 200:
    txt_data = response.text
    
    # Convert the text data to a pandas DataFrame
    data = pd.read_csv(StringIO(txt_data), sep='\s+', comment='#', header=None)

    data.columns = [
        "Year",
        "Annual Mean CO2 Growth Rate",
        "Uncertainty",
    ]

    # Print the first few rows of the DataFrame
    print(data.head())

else:
    print(f"Error fetching data: {response.status_code}")    