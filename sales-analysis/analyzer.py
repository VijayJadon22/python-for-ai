import os

print("Current Directory",os.getcwd())

#check if our data files exists
data_path="data/sales.csv"

if os.path.exists(data_path):
    print(f"Found {data_path}")
else:
    print("Data Not Found")
