import pandas as pd
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_file = os.path.join(base, "data", "raw", "ecommerce_sales.csv")
output_file = os.path.join(base, "data", "cleaned", "ecommerce_sales_cleaned.csv")

df = pd.read_csv(input_file)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df = df.drop_duplicates()

df["Product"] = df["Product"].str.strip()
df["Category"] = df["Category"].str.strip()

os.makedirs(os.path.dirname(output_file), exist_ok=True)

df.to_csv(output_file, index=False)

print("Cleaning completed!")
print(df.head())
print("Shape:", df.shape)