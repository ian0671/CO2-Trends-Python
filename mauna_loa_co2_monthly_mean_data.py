# Author: Ian Knightly
# Date: 2025-04-04
# Version: 1.0
# License: MIT License
# description: 
# This script fetches the Mauna Loa CO2 monthly mean data from NOAA, processes it, and handles missing values.
# It also groups the data by year and calculates the average CO2 concentration and uncertainty for each year.



import numpy as np
import pandas as pd
import requests
from io import StringIO

url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"
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
        "De-seasonalized",
        "Days",
        "Std Dev of Days",
        "Monthly Mean Uncertainty"
    ]

    # Replace invalid values in "Monthly Mean CO2 Uncertainty" with the median
    median_unc = data.loc[
        ~((data["Monthly Mean Uncertainty"] == 0) | (data["Monthly Mean Uncertainty"] == -0.99)),
        "Monthly Mean Uncertainty"
    ].median()  # Calculate the median excluding invalid values
    
    data.loc[
        (data["Monthly Mean Uncertainty"] == 0) | (data["Monthly Mean Uncertainty"] == -0.99),
        "Monthly Mean Uncertainty"
    ] = median_unc
    
    median_std = data.loc[~(data["Std Dev of Days"]==-9.99), "Std Dev of Days"].median()
    data.loc[data["Std Dev of Days"]==-9.99, "Std Dev of Days"] = median_std

    median_days = data.loc[~(data["Days"]==-1), "Days"].median()
    data.loc[data["Days"]==-1, "Days"] = median_days

    # Group the data by year (or any other desired interval)
    data["Year"] = data["Decimal Date"].astype(int)  # Extract the year as an integer
    grouped_data = data.groupby("Year").agg({
        "Decimal Date": "mean",  # Average time within each year
        "Monthly Mean CO2": "mean",  # Average CO2 concentration
        "Monthly Mean Uncertainty": "mean"  # Average uncertainty
    })

    # Rename columns for clarity
    grouped_data.rename(columns={
        "Decimal Date": "Yearly Mean Time",
        "Monthly Mean CO2": "Yearly Mean CO2",
        "Monthly Mean Uncertainty": "Yearly Mean Uncertainty"
    }, inplace=True)

    # Merge the grouped data back into the filtered_data DataFrame
    data = data.merge(grouped_data, on="Year", how="left")

    # Print the first few rows of the DataFrame
    print(data.head())

else:
    print(f"Error fetching data: {response.status_code}")