import pandas as pd

data = {
    "name":["alex", "jamie", "sam", "alfie"],
    "attendance in %": [92, 82, 67, 3],
    "grade" : ["B", "C", "B", "F"],
    "passed" : ["passed", "passed", "passed", "failed"]
}

df = pd.DataFrame(data)
print(df)