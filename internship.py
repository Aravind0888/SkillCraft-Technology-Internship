import pandas as pd

# Load the dataset
df = pd.read_csv("SampleSuperstore.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Check data types
print("\nData Types:")
print(df.dtypes)

# Save the cleaned dataset
df.to_csv("Cleaned_SampleSuperstore.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as: Cleaned_SampleSuperstore.csv")