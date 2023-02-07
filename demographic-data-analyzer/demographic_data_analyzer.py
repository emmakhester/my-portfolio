import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'C:\Users\aaron\Desktop\coding\freeCodeCamp certification projects\data-analysis-with-python\demographic-data-analyzer\adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_count = df[df["education"] == "Bachelors"].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = round(bachelor_count / total_count * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # percentage with salary >50K
    high_ed_count = higher_education.shape[0]
    low_ed_count = lower_education.shape[0]
    high_ed_over = higher_education[higher_education["salary"] == ">50K"].shape[0]
    low_ed_over = lower_education[lower_education["salary"] == ">50K"].shape[0]
    higher_education_rich = round(high_ed_over / high_ed_count * 100, 1)
    lower_education_rich = round(low_ed_over / low_ed_count * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df["hours-per-week"] == min_work_hours]
    num_min_workers = min_workers.shape[0]
    min_workers_over = min_workers[min_workers["salary"] == ">50K"].shape[0]

    rich_percentage = round(min_workers_over / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    grouped = df.groupby("native-country")
    earners_percentage = (grouped["salary"].apply(lambda x: (x == ">50K").mean()) * 100).round(1)
    highest_earning_country = earners_percentage.idxmax()
    highest_earning_country_percentage = earners_percentage[highest_earning_country]

    # Identify the most popular occupation for those who earn >50K in India
    high_earners_india = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    occupation_count = high_earners_india.groupby("occupation").size()
    top_IN_occupation = occupation_count.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
