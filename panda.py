import pandas as pd
import csv as c

with open("your mamas cooking recipies.csv", "a", newline="", encoding="utf-8") as file:
    writer = c.writer(file)
    writer.writerow(["Recipe Name", "Ingredient", "Amount"])