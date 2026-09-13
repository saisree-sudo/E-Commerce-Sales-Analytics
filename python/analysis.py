import pandas as pd
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file = os.path.join(base, "data", "cleaned", "ecommerce_sales_cleaned.csv")

df = pd.read_csv(file)

df["Profit_Margin"] = df["Profit"] / df["Sales"] * 100

df["Discount_Band"] = pd.cut(
    df["Discount"],
    bins=[-1, 10, 20, 30, 100],
    labels=["0-10%", "10-20%", "20-30%", "30%+"]
)

print("Sales vs Profit:")
print(
    df.groupby("Product")[["Sales", "Profit", "Profit_Margin"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

print("\nDiscount Analysis:")
print(
    df.groupby("Discount_Band", observed=True)[["Sales", "Profit"]]
    .sum()
)

print("\nRegional Performance:")
print(
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)