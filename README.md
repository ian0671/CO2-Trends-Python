---

# Keeling Curve Analysis in Python

This repository contains a Jupyter Notebook that walks through the creation of the Keeling Curve using Python. The project uses observational data from the [NOAA Mauna Loa Observatory](https://gml.noaa.gov/ccgg/trends/data.html) to visualize trends in atmospheric CO₂ concentrations over time.

## Overview

The Keeling Curve is one of the most iconic representations in climate science—a time series plot that shows the continuous increase in atmospheric CO₂ concentrations as well as its seasonal variations. In this project, I:

- **Acquired the data:** Downloaded the latest CO₂ concentration dataset from the NOAA Mauna Loa Observatory.
- **Preprocessed the data:** Cleaned and formatted the raw data to extract the necessary date and concentration information.
- **Visualized the data:** Used Python libraries to plot the Keeling Curve, capturing both the long-term trend and seasonal fluctuations.
- **Explored insights:** Provided basic trend analysis and visualization techniques to make sense of the atmospheric data.

## Data Source

All data used in this analysis is obtained from the NOAA Mauna Loa Observatory. Check out the data at:  
[https://gml.noaa.gov/ccgg/trends/data.html](https://gml.noaa.gov/ccgg/trends/data.html)

## Additional Sources

[Keeling Curve Wiki](https://en.wikipedia.org/wiki/Keeling_Curve) 

[How CO2 is measured](https://gml.noaa.gov/ccgg/about/co2_measurements.html)

[NOAA/GML calculation of global means](https://gml.noaa.gov/ccgg/about/global_means.html)

[Understanding CO2 and its relation with parts per million (ppm)](https://www.co2meter.com/blogs/news/co2-ppm)



## Prerequisites

Ensure you have Python 3.7 or later and the following Python libraries installed:

- **numpy**
- **pandas**
- **matplotlib**
- **jupyter** (for running the Notebook)

You can install these requirements using pip:

```bash
pip install numpy pandas matplotlib jupyter
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ian0671/CO2-Trends-Python.git
   cd keeling-curve-analysis
   ```

2. **Launch the Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

3. **Open the Notebook:**

   Locate and open `CO2 Trends.ipynb` to explore the project interactively.

## Notebook Structure

The Jupyter Notebook is organized into the following sections:

1. **Introduction:**  
   Explains the significance of the Keeling Curve and provides background information on the NOAA Mauna Loa Observatory data.

2. **Data Acquisition and Preprocessing:**  
   - Instructions on how the dataset was obtained from the NOAA website.
   - Cleaning and structuring the raw data using `pandas` (including handling comments, unwanted rows, or missing values).
   - Conversion of date fields and ensuring the data is in a time series format.

3. **Data Visualization:**  
   - Use of `matplotlib` to create the Keeling Curve plot.
   - Plot customization to highlight the seasonal cycles and long-term trend in CO₂ concentrations.
   - Additional plots (if any) to visualize other aspects of the data analysis.

4. **Analysis and Interpretation:**  
   - Discussion of the observed trends, including the overall rise in CO₂ and seasonal fluctuations.
   - Comments on potential implications related to climate change on a global scale.

## How It Works

- **Data Handling:**  
  The Notebook uses `pandas` to read the dataset, filtering out commentary rows and converting the raw data into a structured DataFrame.
  
- **Plotting the Keeling Curve:**  
  With `matplotlib`, the Notebook produces a clear, well-labeled graph that illustrates the CO₂ concentrations over time. The code adjusts plot parameters (e.g., axis labels, title, grid lines) to enhance readability.

- **Statistical Insights:**  
  While the primary output is the visual curve, additional analysis is performed to show trends and seasonal effects, providing a deeper understanding of the data dynamics.

## Results

Running the Notebook will produce:
- A time-series plot of atmospheric CO₂ concentration, visually representing the Keeling Curve.
- Visual evidence of both the long-term increase of CO₂ in the atmosphere and the cyclical seasonal variations.

## Future Work

Potential extensions for this project include:
- Incorporating more advanced statistical analyses or forecasting models.
- Comparing the Mauna Loa data with other atmospheric measurements from different observatories.
- Adding interactive visualization tools (like Plotly) to enhance the exploration of trends.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
