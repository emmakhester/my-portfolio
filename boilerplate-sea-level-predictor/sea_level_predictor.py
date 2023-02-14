import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'C:\Users\aaron\Desktop\coding\freeCodeCamp certification projects\data-analysis-with-python\boilerplate-sea-level-predictor\epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)
    ax.set_xlabel('Year')

    # Create first line of best fit
    bestfit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(1880, 2051, 1)
    ax.plot(x, bestfit.intercept + (bestfit.slope)*x, 'r', label='fitted line')

    # Create second line of best fit
    df_2000 = df[df['Year'] > 1999]
    newbestfit = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051, 1)
    ax.plot(x2, newbestfit.intercept + (newbestfit.slope)*x2, 'g')
    

    # Add labels and title
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()