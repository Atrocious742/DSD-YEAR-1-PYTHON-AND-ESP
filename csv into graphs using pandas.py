import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('retail_sales_data.csv')

# Convert to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# Create total sales column
df["total_sales"] = df["price"] * df["quantity"]

# ---------- AGGREGATIONS ----------
sales_by_product = df.groupby("product")["total_sales"].sum()
daily_sales = df.groupby("date")["total_sales"].sum()  # assumes 'date' column exists

# ---------- PLOTTING ----------
plt.figure(figsize=(14, 5))

# Graph 1: Bar Chart – Revenue by Product
plt.subplot(1, 2, 1)
sales_by_product.plot(kind="bar", color="skyblue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)

# Graph 2: Line Chart – Daily Revenue Trend
plt.subplot(1, 2, 2)
daily_sales.plot(kind="line", marker="o", color="cyan")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)

plt.tight_layout()
plt.show()

# Group by category
sales_by_category = df.groupby("category")["total_sales"].sum()

# Plot pie chart
plt.figure(figsize=(7, 7))
plt.pie(
    sales_by_category,
    labels=sales_by_category.index,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Revenue Distribution by Category")
plt.tight_layout()
plt.show()