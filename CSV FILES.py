import csv

with open("scores.csv", "a", newline="")as file:
    writer = csv.writer("file")
    writer.writerow(["alex", "10"])