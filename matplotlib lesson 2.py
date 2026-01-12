import kagglehub


path = kagglehub.dataset_download("kvpratama/pokemon-images-dataset")

print("Path to dataset files:", path)

path = kagglehub.dataset_download("vishalsubbiah/pokemon-images-and-types")

print("Path to dataset files:", path)

import csv
with open(path +'pokemon.csv', "r") as f:
    for row in reader:
        print(row)