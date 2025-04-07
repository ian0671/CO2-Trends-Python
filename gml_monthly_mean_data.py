


import numpy as np
import pandas as pd
import requests
from io import StringIO

url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.txt"
response = requests.get(url)

if response.status_code == 200:
    txt_data = response.text
   
    # Convert the text data to a pandas DataFrame
    data = pd.read_csv(StringIO(txt_data), sep='\s+', comment='#', header=None)

    # Assign column names
    data.columns = [
        "Year",
        "Month",
        "Decimal Date",
        "Monthly Mean CO2",
        "Monthly Mean Uncertainty",
        "De-seasonalized",
        "De-seasonalized Uncertainty"
    ]


    # Print the first few rows of the DataFrame
    print(data.head())

else:
    print(f"Error fetching data: {response.status_code}")