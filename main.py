import pandas as pd

fileLoc = "../Pandas/vgsales.csv"
read = pd.read_csv(fileLoc)
print(read.head())