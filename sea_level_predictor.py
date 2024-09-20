import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df =pd.read_csv("epa-sea-level.csv")
    x= df['Year']
    y= df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    result = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = result.slope * x_pred + result.intercept
    plt.plot(x_pred, y_pred, "r")

    # Create second line of best fit
    df_2 = df[df['Year'] >= 2000]
    x_2= df_2['Year']
    y_2= df_2['CSIRO Adjusted Sea Level']    

    result_2 = linregress(x_2,y_2)
    x_pred_2 = pd.Series([i for i in range(2000,2051)])
    y_pred_2 = result_2.slope * x_pred_2 + result_2.intercept
    plt.plot(x_pred_2, y_pred_2, "green")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()