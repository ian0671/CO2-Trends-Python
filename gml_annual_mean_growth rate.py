import pandas as pd
import requests
from io import StringIO

url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_gl.txt"
response = requests.get(url)

if response.status_code == 200:
    txt_data = response.text
    
    # Convert the text data to a pandas DataFrame
    data = pd.read_csv(StringIO(txt_data), sep='\s+', comment='#', header=None)

    data.columns = [
        "Year",
        "Annual Increase in CO2",
        "Uncertainty",
    ]

    # Print the first few rows of the DataFrame
    print(data.head())

else:
    print(f"Error fetching data: {response.status_code}")    