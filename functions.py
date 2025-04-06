# Title: CO2 Concentration Model Fitting
# Author: Ian Knightly
# Date: 2025-04-04
# Version: 1.0
# License: MIT License

# Description: 
# This script fits a generalized polynomial model to CO2 concentration data
# using the scipy library. It allows for flexible polynomial fitting by               
# accepting a variable number of parameters, which can be adjusted to fit
# different degrees of polynomial models. The script also includes functions to
# calculate the reduced chi-squared statistic and the residuals between the
# observed data and the model predictions. The fitting process is performed using
# the curve_fit function from scipy.optimize, which provides a robust way to
# estimate the parameters of the model based on the observed data and their
# uncertainties. The script is designed to be modular and reusable, allowing for
# easy integration into larger data analysis workflows or for standalone use.
# The model can be applied to various datasets, making it a versatile tool for
# researchers and analysts working with CO2 concentration data or similar time
# series data. The script is intended for educational and research purposes and 
# can be modified to suit specific needs or to incorporate additional features as required.

# Import necessary libraries
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt


# This function fits a generalized polynomial model to CO2 concentration data
# using the scipy library. It allows for flexible polynomial fitting by
# accepting a variable number of parameters, which can be adjusted to fit

def generalized_model(x, *params):
    """
    Generalized polynomial model with variable parameters.
    The number of parameters determines the degree of the polynomial.

    Parameters:
    - x: Independent variable (e.g., time or year)
    - *params: Coefficients of the polynomial (p0, p1, ..., pn)

    Returns:
    - The polynomial value for the given x and parameters.
    """
    return sum(p * x**i for i, p in enumerate(params))

def fit_model(X, Y, Y_error, initial_guesses):
    """
    Fits a generalized model to the data using curve_fit.

    Parameters:
    - X: Independent variable (e.g., time or year)
    - Y: Dependent variable (e.g., CO2 concentration)
    - Y_error: Uncertainty in Y
    - initial_guesses: Initial guesses for the parameters

    Returns:
    - params: Fitted parameters
    - uncertainties: Uncertainties in the fitted parameters
    - fitted_curve: The fitted curve values for X
    """
    # Fit the model using curve_fit
    params, covariance = curve_fit(
        generalized_model, X, Y, p0=initial_guesses, sigma=Y_error, absolute_sigma=True
    )
    uncertainties = np.sqrt(np.diag(covariance))  # Calculate uncertainties
    fitted_curve = generalized_model(X, *params)  # Generate the fitted curve
    
    return params, uncertainties, fitted_curve


# This function calculates the reduced chi-squared statistic for the fit
# and can be used to evaluate the goodness of fit.

def reduced_chi_sqr(Y, Y_err, Y_model, Params):
    """
    Calculate the reduced chi-squared statistic.
    
    Parameters:
    Y (array-like): Observed data.
    Y_err (array-like): Uncertainties in the observed data.
    Y_model (array-like): Model predictions.
    
    Returns:
    float: Reduced chi-squared statistic.
    """
    # Calculate the chi-squared statistic
    chi2 = np.sum(((Y - Y_model) / Y_err) ** 2)
    
    # Calculate the degrees of freedom
    dof = len(Y) - Params  # Number of data points minus number of parameters
    
    # Calculate the reduced chi-squared statistic
    return chi2 / dof if dof > 0 else np.inf


# This function calculates the residuals between the observed data and the
# model predictions. It can be used to assess the fit visually or numerically.

def residuals(Y, Y_model):
    """
    Calculate the residuals between observed and model data.

    Parameters:
    - Y: Observed data
    - Y_model: Model predictions

    Returns:
    - Residuals (Y - Y_model)
    """
    return Y - Y_model