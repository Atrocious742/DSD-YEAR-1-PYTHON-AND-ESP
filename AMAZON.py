import csv
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("amazon_sales_dataset.csv")
print(df.head())
print(df.info())

#calculate the total sales and average sales value
total_sales = df['total_revenue'].sum()
average_sales = df['total_revenue'].mean() 
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")

# Bar chart of the sales by category

category_sales = df.groupby('product_category')['total_revenue'].sum()
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color='green')
plt.title('Total Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()

#sales by region 

region_sales = df.groupby('customer_region')['total_revenue'].sum()
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color='orange')
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()

#scatter of discount and quantity sold
plt.figure(figsize=(10, 6))
plt.scatter(df['discount_percent'], df['quantity_sold'], color='purple')
plt.title('Discount vs Quantity Sold')
plt.xlabel('Discount')
plt.ylabel('Quantity Sold')
plt.tight_layout()
plt.show()