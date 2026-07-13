import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Excel Dataset
# ==========================
df = pd.read_excel("marketing_campaign_dataset.xlsx")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe(include="all"))

# ==========================
# Chart 1
# Campaign Type Count
# ==========================
plt.figure(figsize=(8,5))
df["Campaign_Type"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Number of Campaigns by Campaign Type")
plt.xlabel("Campaign Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Chart1_Campaign_Type.png")
plt.show()

# ==========================
# Chart 2
# Average ROI by Channel
# ==========================
plt.figure(figsize=(8,5))
df.groupby("Channel_Used")["ROI"].mean().plot(kind="bar", color="green")
plt.title("Average ROI by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Average ROI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Chart2_ROI_Channel.png")
plt.show()

# ==========================
# Chart 3
# Conversion Rate
# ==========================
plt.figure(figsize=(8,5))
df.groupby("Campaign_Type")["Conversion_Rate"].mean().plot(kind="bar", color="orange")
plt.title("Average Conversion Rate by Campaign Type")
plt.xlabel("Campaign Type")
plt.ylabel("Conversion Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Chart3_Conversion_Rate.png")
plt.show()

# ==========================
# Chart 4
# Clicks vs Impressions
# ==========================
plt.figure(figsize=(8,5))
plt.scatter(df["Impressions"], df["Clicks"], alpha=0.3)
plt.title("Clicks vs Impressions")
plt.xlabel("Impressions")
plt.ylabel("Clicks")
plt.tight_layout()
plt.savefig("Chart4_Clicks_Impressions.png")
plt.show()

print("\n===================================")
print("TASK 4 COMPLETED SUCCESSFULLY!")
print("Charts saved in your Data Analyst folder.")
print("===================================")