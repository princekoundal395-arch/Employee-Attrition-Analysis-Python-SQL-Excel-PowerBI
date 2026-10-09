"""
==============================================================
EMPLOYEE ATTRITION ANALYSIS - PYTHON CLEANING + EDA (STEP 1 of 4)
==============================================================
Pipeline: Python (this script) -> SQL -> Excel -> Power BI

Is script mein do parts hain:
PART A: Data Cleaning (raw messy data ko clean karna)
PART B: Exploratory Data Analysis / EDA (cleaned data se
        initial patterns dhundna, taaki SQL/Excel/Power BI
        mein kya analyze karna hai iska pata chale)
==============================================================
"""

import pandas as pd

# ==============================================================
# PART A: DATA CLEANING
# ==============================================================

# ------------------------------------------------------------
# STEP 1: Load raw data
# ------------------------------------------------------------
df = pd.read_csv("data/hr_employee_data_raw.csv")
print("STEP 1: Raw data loaded")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

# ------------------------------------------------------------
# STEP 2: Inspect the data quality issues
# ------------------------------------------------------------
print("STEP 2: Missing values per column")
print(df.isnull().sum()[df.isnull().sum() > 0], "\n")
print("Duplicate rows found:", df.duplicated().sum(), "\n")

# ------------------------------------------------------------
# STEP 3: Remove exact duplicate rows
# ------------------------------------------------------------
before = len(df)
df = df.drop_duplicates()
print(f"STEP 3: Removed {before - len(df)} duplicate rows. New shape: {df.shape}\n")

# ------------------------------------------------------------
# STEP 4: Standardize text columns (casing + whitespace)
# ------------------------------------------------------------
text_cols = ["gender", "marital_status", "department", "job_role", "over_time", "business_travel"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()
    df[col] = df[col].replace("Nan", pd.NA)

# fix abbreviations that Title Case incorrectly reformats (Hr -> HR, It -> IT)
df['department'] = df['department'].replace({"Hr": "HR", "It": "IT", "R&D": "R&D"})
df['job_role'] = df['job_role'].str.replace(r'\bHr\b', 'HR', regex=True)
df['job_role'] = df['job_role'].str.replace(r'\bIt\b', 'IT', regex=True)
df['job_role'] = df['job_role'].str.replace(r'\bR&D\b', 'R&D', regex=True)

# fix known casing edge cases Title Case can mishandle
df['over_time'] = df['over_time'].replace({"Yes": "Yes", "No": "No"})
df['business_travel'] = df['business_travel'].replace({
    "Travel_Rarely": "Travel_Rarely", "Travel_Frequently": "Travel_Frequently", "Non-Travel": "Non-Travel"
})
print("STEP 4: Text columns cleaned (casing/whitespace standardized)\n")

# ------------------------------------------------------------
# STEP 5: Fix invalid / out-of-range values
# ------------------------------------------------------------
# age should realistically be between 18 and 65
invalid_age_count = ((df['age'] < 18) | (df['age'] > 65)).sum()
df.loc[(df['age'] < 18) | (df['age'] > 65), 'age'] = pd.NA
print(f"STEP 5a: Found and nulled {invalid_age_count} invalid age values (outside 18-65)")

# monthly_income cannot be negative
invalid_income_count = (df['monthly_income'] < 0).sum()
df.loc[df['monthly_income'] < 0, 'monthly_income'] = pd.NA
print(f"STEP 5b: Found and nulled {invalid_income_count} invalid (negative) income values\n")

# ------------------------------------------------------------
# STEP 6: Handle missing values
# ------------------------------------------------------------
print("STEP 6: Missing values before final handling:")
print(df.isnull().sum()[df.isnull().sum() > 0], "\n")

# Numeric columns -> fill with median (robust to outliers, unlike mean)
for col in ['age', 'monthly_income', 'job_satisfaction']:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)

# Categorical column -> fill with "Unknown"
df['department'] = df['department'].fillna("Unknown")

print("STEP 6b: Missing values after handling:")
print(df.isnull().sum().sum(), "total missing values remain\n")

# ------------------------------------------------------------
# STEP 7: Correct data types
# ------------------------------------------------------------
df['age'] = df['age'].astype(int)
df['monthly_income'] = df['monthly_income'].astype(int)
df['job_satisfaction'] = df['job_satisfaction'].astype(int)
print("STEP 7: Data types corrected\n")

# ------------------------------------------------------------
# STEP 8: Save cleaned data
# ------------------------------------------------------------
df = df.reset_index(drop=True)
df.to_csv("hr_employee_data_cleaned.csv", index=False)
print(f"STEP 8: Cleaned data saved. Final shape: {df.shape}\n")


# ==============================================================
# PART B: EXPLORATORY DATA ANALYSIS (EDA)
# ==============================================================
print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Overall attrition rate
attrition_rate = round((df['attrition'] == 'Yes').mean() * 100, 2)
print(f"\nOverall Attrition Rate: {attrition_rate}%")

# Attrition by department
print("\nAttrition Rate by Department:")
dept_attrition = df.groupby('department')['attrition'].apply(
    lambda x: round((x == 'Yes').mean() * 100, 2)
).sort_values(ascending=False)
print(dept_attrition)

# Attrition by overtime
print("\nAttrition Rate by OverTime:")
ot_attrition = df.groupby('over_time')['attrition'].apply(
    lambda x: round((x == 'Yes').mean() * 100, 2)
)
print(ot_attrition)

# Average job satisfaction: stayed vs left
print("\nAverage Job Satisfaction (1-4 scale):")
print(df.groupby('attrition')['job_satisfaction'].mean().round(2))

# Average monthly income: stayed vs left
print("\nAverage Monthly Income:")
print(df.groupby('attrition')['monthly_income'].mean().round(0))

# Correlation between years at company and attrition (as numeric)
df['attrition_flag'] = (df['attrition'] == 'Yes').astype(int)
print("\nCorrelation of numeric features with Attrition:")
numeric_cols = ['age', 'monthly_income', 'years_at_company', 'job_satisfaction',
                'work_life_balance', 'distance_from_home', 'attrition_flag']
print(df[numeric_cols].corr()['attrition_flag'].sort_values(ascending=False))

print("\nEDA complete. Insights above guide what to explore further in SQL/Excel/Power BI.")
