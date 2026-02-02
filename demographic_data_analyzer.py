import pandas as pd

def calculate_demographics(df):
    # Strip whitespace from string columns to avoid mismatches
    df['native-country'] = df['native-country'].str.strip()
    df['salary'] = df['salary'].str.strip()
    
    # 1. Number of each race
    race = df['race'].value_counts()
    
    # 2. Average age of men
    maleAgeAvg = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. Percentage with Bachelors degrees
    bachlorDeg = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # 4. Percentage with higher education earning >50K
    advEdu_mask = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    advEdu_rich = df[advEdu_mask & (df['salary'] == '>50K')]
    advEdu = round(len(advEdu_rich) * 100 / advEdu_mask.sum(), 1) if advEdu_mask.sum() > 0 else 0
    
    # 5. Percentage without higher education earning >50K
    notAdvEdu_mask = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    notAdvEdu_rich = df[notAdvEdu_mask & (df['salary'] == '>50K')]
    NotadvEdu = round(len(notAdvEdu_rich) * 100 / notAdvEdu_mask.sum(), 1) if notAdvEdu_mask.sum() > 0 else 0
    
    # 6. Minimum work hours per week
    minHoursWeek = df['hours-per-week'].min()
    
    # 7. Percentage of people who work minimum hours and earn >50K
    minHour_rich = df[(df['hours-per-week'] == minHoursWeek) & (df['salary'] == '>50K')]
    minWorkSal = round(len(minHour_rich) * 100 / len(df[df['hours-per-week'] == minHoursWeek]), 1) if len(df[df['hours-per-week'] == minHoursWeek]) > 0 else 0
    
    # 8. Country with highest percentage of people earning >50K
    country_counts = df.groupby('native-country').size()
    rich_counts = df[df['salary'] == '>50K'].groupby('native-country').size()
    rich_percentage = (rich_counts / country_counts) * 100
    rich_percentage = rich_percentage.dropna()
    if not rich_percentage.empty:
        highest_country = rich_percentage.idxmax()
        highest_percentage = round(rich_percentage.max(), 1)
    else:
        highest_country = None
        highest_percentage = None
    
    # 9. Most popular occupation for those earning >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupation_counts = india_rich['occupation'].value_counts()
    if not occupation_counts.empty:
        top_occupation = occupation_counts.idxmax()
    else:
        top_occupation = None
    
    # Print all results
    print("Number of each race:\n", race, "\n")
    print("Average age of men:", maleAgeAvg)
    print("Percentage with Bachelors degrees:", bachlorDeg)
    print("Percentage with higher education earning >50K:", advEdu)
    print("Percentage without higher education earning >50K:", NotadvEdu)
    print("Minimum work hours per week:", minHoursWeek)
    print("Percentage of rich among those who work minimum hours:", minWorkSal)
    print("Country with highest percentage of rich:", highest_country)
    print("Highest percentage of rich people in country:", highest_percentage)
    print("Most popular occupation in India for those earning >50K:", top_occupation)


# Example data (you can replace this with the full dataset)
data = {
    "age": [39, 50, 38, 53, 28, 45],
    "workclass": ["State-gov", "Self-emp-not-inc", "Private", "Private", "Private", "Private"],
    "fnlwgt": [77516, 83311, 215646, 234721, 338409, 200000],
    "education": ["Bachelors", "Bachelors", "HS-grad", "11th", "Bachelors", "Masters"],
    "education-num": [13, 13, 9, 7, 13, 14],
    "marital-status": ["Never-married", "Married-civ-spouse", "Divorced", "Married-civ-spouse", "Married-civ-spouse", "Married-civ-spouse"],
    "occupation": ["Adm-clerical", "Exec-managerial", "Handlers-cleaners", "Handlers-cleaners", "Prof-specialty", "Prof-specialty"],
    "relationship": ["Not-in-family", "Husband", "Not-in-family", "Husband", "Wife", "Husband"],
    "race": ["White", "White", "White", "Black", "Black", "Asian-Pac-Islander"],
    "sex": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "capital-gain": [2174, 0, 0, 0, 0, 5000],
    "capital-loss": [0, 0, 0, 0, 0, 0],
    "hours-per-week": [40, 13, 40, 40, 40, 45],
    "native-country": ["United-States", "United-States", "United-States", "United-States", "Cuba", "India"],
    "salary": ["<=50K", "<=50K", "<=50K", "<=50K", "<=50K", ">50K"]
}

df = pd.DataFrame(data)
calculate_demographics(df)
