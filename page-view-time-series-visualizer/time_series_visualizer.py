import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"C:\Users\aaron\Desktop\coding\freeCodeCamp certification projects\data-analysis-with-python\page-view-time-series-visualizer\fcc-forum-pageviews.csv", parse_dates=['date'])
df = df.set_index('date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]
df = df.rename(columns={'value' : 'Page Views'})

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(20,5))
    plt.plot(df, color='r', figure=fig)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.month_name() for d in df_bar.date]
    grouped = df_bar.groupby(['year', 'month'])['Page Views'].mean()
    grouped = grouped.reset_index()
    grouped = grouped.rename(columns={'month' : 'Months', 'year' : 'Years', 'Page Views' : 'Average Page Views'})


    # Draw bar plot
    fig, ax = plt.subplots()
    palette = sns.color_palette('Paired', 12)
    fig = sns.catplot(data=grouped, x='Years', y='Average Page Views', kind='bar', hue='Months', hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], palette=palette).figure

    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box = df_box.rename(columns={'year' : 'Year', 'month' : 'Month'})


    fig, ax = plt.subplots(1, 2, figsize=(20, 5))
    sns.boxplot(data=df_box, x="Year", y="Page Views", ax=ax[0])
    sns.boxplot(data=df_box, x="Month", y="Page Views", ax=ax[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
