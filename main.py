import csv
import pandas as pd

with open("active_products.csv") as file:
    active_products = csv.reader(file)

    list_of_active_pr = []

    for row in active_products:
        list_of_active_pr.append(row[4])

stock_list = []

stock = pd.read_csv("stock.csv", encoding="mac_roman", delimiter=";")
for row in stock["Title"]:
    stock_list.append(row)

inactive_bottles_list = []

for bottle in stock_list:
    if bottle not in list_of_active_pr:
        inactive_bottles_list.append(bottle)
    else:
        continue

tasting_samples = [s for s in inactive_bottles_list if "(Tasting sample)" in s]
tasting_Samples = [s for s in inactive_bottles_list if "(Tasting Sample)" in s]

DBM = []
for dbm in inactive_bottles_list:
    if dbm.find("Deer, Bear & Moose") != -1:
        DBM.append(dbm)
for dbm in DBM:
    inactive_bottles_list.remove(dbm)

for samples in tasting_samples:
   inactive_bottles_list.remove(samples)

for Samples in tasting_Samples:
    inactive_bottles_list.remove(Samples)

for inactive_bottle in inactive_bottles_list:
    print(inactive_bottle)
print(f"Number of inactive bottles: {len(inactive_bottles_list)}\n")

print("Please note that number might be higher because of included:\Vault bottles, weird characters and metabase discrepancies (some bottles are actually active).")
