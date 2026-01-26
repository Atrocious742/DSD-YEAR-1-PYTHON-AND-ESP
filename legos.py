import pandas as pd
import csv as c
import matplotlib.pyplot as plt

df = pd.read_csv("lego_sets.csv")
print(df.head())
print(df.info)

average_price = df['list_price'].mean()
print("average price of lego is: "+str(average_price))

maximum_price = df["list_price"].max()
print("maximum price of a lego set is:"+str(maximum_price))


plt.plot(df['list_price'])
plt.xlabel('lego sets')
plt.ylabel('lego prices')
plt.show()


plt.scatter(df['piece_count'], df['list_price'], alpha=0.6)
plt.xlabel('peice count')
plt.ylabel('price')
plt.scatter
plt.show()

top_themes = (
    df.groupby('theme_name')['star_rating']
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

top_themes.plot(kind='bar', figsize=(10, 5), title='Top 10 Themes by Average Rating')

plt.figure(figsize=(10, 5))
top_themes.plot(kind='bar')
plt.ylabel('Average Star Rating')
plt.title('Top 10 Themes by Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()