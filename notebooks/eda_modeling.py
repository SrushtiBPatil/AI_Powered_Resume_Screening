import pandas as pd

# Load dataset
df = pd.read_csv('D:/Resume_matcher/data/fake_job_postings.csv')

# Preview shape and first few rows
print("Shape of dataset:", df.shape)
print(df.head(3))

# Check for missing values
print("\nMissing values per column:\n")
print(df.isnull().sum())

# Check data types
print("\nData types:\n")
print(df.dtypes)

# Check class balance for target variable
print("\nFraudulent value counts:\n")
print(df['fraudulent'].value_counts())

# Check the % of fraudulent posts
fraud_percent = df['fraudulent'].mean() * 100
print(f"\nPercentage of fraudulent postings: {fraud_percent:.2f}%")
# Drop job_id
df.drop(columns=['job_id'], inplace=True)

# Fill missing text-based columns with empty strings
text_cols = ['company_profile', 'description', 'requirements', 'benefits',
             'department', 'salary_range', 'employment_type', 
             'required_experience', 'required_education', 'industry', 'function', 'location']

for col in text_cols:
    df[col] = df[col].fillna('')

# Confirm no missing values now
print("\nRemaining missing values (should be 0):")
print(df.isnull().sum().sum())
