import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("sales_data.csv")
print(df.head())
print(df.info())
print(df.sum())

print(df.isnull())

df["Revenue"] = df["Quantity"] * df["Unit_Price"]
print(df[["Product_Category", "Quantity", "Unit_Price", "Revenue"]])

revenue_by_category = df.groupby("Product_Category")["Revenue"].sum()

print(revenue_by_category)

revenue_by_category = revenue_by_category.reset_index()
print(revenue_by_category)

plt.bar(df["Quantity"], df["Unit_Price"])
plt.show()