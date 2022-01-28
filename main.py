import csv
import pandas as pd

with open("active_products.csv") as file:
    reader = csv.reader(file)

    list_of_active_pr = []

    for row in reader:
        list_of_active_pr.append(row[4])

stock_list = []

stock = pd.read_csv("stock.csv", encoding="mac_roman", delimiter=";") #if using Windows, use encoding="cp1252"
for row in stock["Title"]:
    stock_list.append(row)

inactive_bottles_list = []

for bottle in stock_list:
    if bottle not in list_of_active_pr:
        inactive_bottles_list.append(bottle)
    else:
        continue


for inactive_bottle in inactive_bottles_list:
    print(inactive_bottle)
print(f"Number of inactive bottles: {len(inactive_bottles_list)}\n")

print("Please note that number might be higher because of included:\ntasting samples, Vault bottles, weird characters and metabase discrepancies (some bottles are actually active)")
