import pandas as pd

fileLoc = "../Pandas/vgsales.csv"
data = pd.read_csv(fileLoc)
data = pd.DataFrame(data)

# Make the Rank column to serve as Index ! 
data.set_index("Rank" , inplace = True)

#  .head() is used to print only 5 rows , whereas without this , whole date will print !
print("\n5 Rows from start : \n\n" ,  data.head(5))

#  .tail() is used to print only 5 rows from end , whereas without this , whole date will print !
print("\n5 Rows from last : \n\n" , data.tail(5))

# To extract all columns
colms = data.columns
print(colms)

# print(data["Rank"].max())
print(data[colms[0]].head())

print(data.index.max())

# To make spreadsheet , and for this openpyxl is required to install (pip install openpyxl)
sheet = data.to_excel("VgSales.xlsx" , sheet_name = "VgSales_data" , index = False)