
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("customer_churn.csv")

# Display first five records
print("First five records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values with the median
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with the mode
for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Analyze customer churn
if "Churn" in df.columns:
    print("\nChurn Distribution:")
    print(df["Churn"].value_counts())

    print("\nChurn Percentage:")
    print(df["Churn"].value_counts(normalize=True) * 100)

# Analyze churn by contract type
if "Contract" in df.columns and "Churn" in df.columns:
    print("\nChurn by Contract:")
    print(pd.crosstab(df["Contract"], df["Churn"]))

# Analyze churn by payment method
if "PaymentMethod" in df.columns and "Churn" in df.columns:
    print("\nChurn by Payment Method:")
    print(pd.crosstab(df["PaymentMethod"], df["Churn"]))

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully.")
