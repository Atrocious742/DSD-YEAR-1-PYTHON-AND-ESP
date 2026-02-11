import pandas as pd
import csv
df = pd.read_csv("pixelvault game sales.csv")
print(df.head())
print(df.tail())
print(df.notna())

most_popular_game = df['game_title'].mode()[0]
print("Most popular game is: " + most_popular_game)

most_popular_catergory = df['category'].mode()[0]
print("Most popular category is: " + most_popular_catergory)

highest_single_total_sales = df['total_sale'].max()
print("Highest single total sales is: " + str(highest_single_total_sales))

Average_total_sales = df['total_sale'].mean()
print("Average total sales is: " + str(Average_total_sales))
