import os
import pandas as pd


print("Current Directory",os.getcwd())

#check if our data files exists
data_path="data/sales.csv"

if os.path.exists(data_path):
    print(f"Found {data_path}")
else:
    print("Data Not Found")

#--------------------------------------------------------
# Now we are going to do tasks

df=pd.read_csv("data/sales.csv")
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")


# Quick operation: calculate total for each row
df["Total"]=df["quantity"]*df["price"]
print("\nWith totals:")
print(df)