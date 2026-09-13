import pandas as pd
import matplotlib.pyplot as plt
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file = os.path.join(base, "data", "cleaned", "ecommerce_sales_cleaned.csv")

df = pd.read_csv(file)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nCategory Performance:")
print(df.groupby("Category")[["Sales", "Profit"]].sum())

print("\nTop Products:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10))

monthly = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()

monthly.plot(kind="line", marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()