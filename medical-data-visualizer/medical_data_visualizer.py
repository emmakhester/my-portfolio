import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r"C:\Users\aaron\Desktop\coding\freeCodeCamp certification projects\data-analysis-with-python\medical-data-visualizer\medical_examination.csv")

# Add 'overweight' column
df['bmi'] = (df['weight'] / ((df['height'] / 100) ** 2))
df['overweight'] = np.where(df['bmi'] > 25, 1, 0)
df = df.drop(columns='bmi')

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    grp = df_cat.groupby(["cardio", "variable"])['value'].value_counts()
    grp = grp.reset_index(name="total")

    # Draw the catplot with 'sns.catplot()'
    fig, ax = plt.subplots()
    fig = sns.catplot(data=grp, x='variable', y='total', kind='bar', hue='value', col='cardio').fig


    # Get the figure for the output


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]


    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool_)
    mask[np.triu_indices_from(mask)] = True
 

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
