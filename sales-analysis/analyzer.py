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

#create an output directory if not already exists

os.makedirs("output",exist_ok=True)

#Save as different formats
#1. JSON format good for web API's
df.to_json("output/sales.json",orient="records")

# 2. Excel format (good for sharing)
df.to_excel("output/sales.xlsx",index=False)


# 3. Updated CSV (with our new total column)
df.to_csv("output/sales.csv",index=False)