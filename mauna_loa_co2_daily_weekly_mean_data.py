


import numpy as np
import pandas as pd
import requests
from io import StringIO

# Processing the weekly data
weekly_url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_weekly_mlo.txt"
weekly_response = requests.get(weekly_url)

if weekly_response.status_code == 200:
    weekly_txt_data = weekly_response.text
    
    # Convert the text data to a pandas DataFrame
    weekly_data = pd.read_csv(StringIO(weekly_txt_data), sep='\s+', comment='#', header=None)

    weekly_data.columns = [
        "Year",
        "Month",
        "Week",
        "Decimal Date",
        "CO2 Molar Fraction (ppm)",
        "Number of Days",
        "1 Year Ago",
        "10 Year Ago",
        "Increase Since 1800"
    ]

    # Print the first few rows of the DataFrame
    # print(weekly_data.head())

else:
    print(f"Error fetching data: {weekly_response.status_code}") 

# Processing the daily data
daily_url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_daily_mlo.txt"
daily_response = requests.get(daily_url)

if daily_response.status_code == 200:
    daily_txt_data = daily_response.text
    
    # Convert the text data to a pandas DataFrame
    daily_data = pd.read_csv(StringIO(daily_txt_data), sep='\s+', comment='#', header=None)

    daily_data.columns = [
        "Year",
        "Month",
        "Day",
        "Decimal Date",
        "CO2 Molar Fraction (ppm)",
    ]

    # Print the first few rows of the DataFrame
    # print(daily_data.head())

else:
    print(f"Error fetching data: {daily_response.status_code}")
    
# Merge the grouped data back into the filtered_data DataFrame

data = weekly_data.merge(daily_data, on="Year", how="left")

# Print the first few rows of the DataFrame
print(data.head())    