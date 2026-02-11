import pandas as pd
import matplotlib.pyplot as plt
import csv

#read all csv files into a list of dataframes
df1 = pd.read_csv('WinterSD.csv')
df2 = pd.read_csv('SummerSD.csv')
df3 = pd.read_csv('CountriesSD.csv')

#make a graph comparing the data from the three dataframes
plt.figure(figsize=(10, 6))
plt.plot(df1['Year'], df1['Value'], label='WinterSD', color='blue')
plt.plot(df2['Year'], df2['Value'], label='SummerSD', color='orange')
plt.plot(df3['Year'], df3['Value'], label='CountriesSD', color='green')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Comparison of WinterSD, SummerSD, and CountriesSD over Years')
plt.legend()
plt.grid()
plt.show()