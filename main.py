import csv
import pandas as pd

with open("active_products.csv", encoding = "utf-8") as file:
    active_products = csv.reader(file)

    list_of_active_pr = []

    for row in active_products:
        list_of_active_pr.append(row[4])

stock_list = []

stock = pd.read_csv("stock.csv", encoding="utf-8", delimiter=";")
for row in stock["Title"]:
    stock_list.append(row)

inactive_bottles_list = []

for bottle in stock_list:
    if bottle not in list_of_active_pr:
        inactive_bottles_list.append(bottle)
    else:
        continue

vault = ["Ardbeg 1975 Gordon and MacPhail", "Ardbeg Traigh Bhan 19 Year Old 2020 Edition", "Blanton’s Single Barrel Dumped 2019 46.5%", "Blanton’s Single Barrel Dumped 2019 64.6%",
         "Blanton’s Single Barrel Dumped 2019 64.8%", "Bowmore 1991 Antique Lions 25 Year Old The Butterflies Series", "Brora 1975 20 Year Old Rare Malt (200ml)",
         "Brora 1977 24 Year Old Rare Malt", "Brora 1981 Douglas Laing 21 Year Old", "Bruichladdich Octomore 1.1", "Cadenhead’s Bruichladdich 25 Year Old 1968",
         "Chapter 7 Monologue 24 Year Old Ledaig 1995", "Chichibu 2009 Original Quarter Cask No.388", "D’Aincourt Cognac Extra (Wooden Box)", "D’Aincourt Cognac Premier Cru",
         "Eagle Rare 10 Year Old Single Barrel", "Faustino V Reserva 1970 Rioja", "Finca El Cipres Natural Coffee Bag", "Frérot Cognac XO Assemblage de Crus", "George T. Stagg Kentucky Straight Bourbon Whiskey 2017 Release",
         "Glenfiddich Snow Phoenix", "Glenmorangie 22 Year Old 1971", "Gordon & MacPhail Glen Grant 1990", "Hibiki 21 Year Old", "Highland Park 24 Year Old 1989 Càrn Mòr",
         "Highland Park 30 Year Old Scotch Whisky", "Ichiro’s Malt Chichibu The First Ten 2020", "Jack Daniel’s Guitar Pack Special Edition", "John Scott’s 35 Year Old Superior Blended Scotch",
         "Karuizawa Hanshin Tigers Champions 2003", "Kraken Black Spiced Rum Limited Edition Decanter", "Lagavulin 11 Year Old Nick Offerman 2019 Edition", "Lagavulin 1980 Pedro Ximénez Cask Finish Distillers Edition",
         "Larga Vida XO Rum 2018 Edition", "Mai Tai Nio Cocktail", "Marquis De Montesquiou 1972 Armagnac", "Murray McDavid Mission 21 Year Old Rosebank 1990",
         "Murray McDavid Mission Islay Trilogy 1969", "Pappy Van Winkle’s Family Reserve Bourbon 15 Year Old", "Port Ellen 21 Year Old 1980 Silver Seal (Sestante Collection)",
         "Port Ellen 27 Year Old 1978", "Queen of the South 8 Year Old", "Rare Malts Rosebank 22 Year Old 1981", "Ron de Jeremy", "Ron de Jeremy Holy Wood 18 Year Old Bourbon Cask",
         "Ron de Jeremy Holy Wood 20 Year Old Malt Whisky Barrel", "Rosebank 21 Year Old 1990", "Royal Lochnagar Selected Reserve", "Royal Lochnagar The Distillers Edition 1998 Muscat Cask Finish",
         "Rum XO III 0.5l", "Sazerac Straight Rye Whiskey", "Skarucna Serpent’s Spit", "Son of a Peat Batch 01", "Son of a Peat Batch 02", "Son of a Peat Batch 03 The Redeemer",
         "Specialty Drinks Laphroaig 20 Year Old 1996", "Tamdhu 10 Year Old (Old Bottling)", "The Balvenie A Day of Dark Barley 26 Year Old",
         "The Balvenie Tun 1509 Batch #1", "The Dalmore 27 Year Old 1992 Cask Strength Collection", "The GlenDronach 26 Year Old 1993", "The Glenlivet 12 Year Old 1960s",
         "The Macallan 12 Year Old 1980s (Giovinetti Import)", "The Macallan 18 Year Old 1990 Sherry Oak", "Vault Selection IX.", "Vault Selection VIII.", "Very Olde St. Nick Cask Strength Summer Rye",
         "Tullibardine 10 Year Old", "Viuva Jose Gomes da Silva & Filhos Collares Genuino 1962", "WhiskySponge 27 Year Old 1992 Edition No.17", "Yamazaki 12 Year Old",
         "Yoichi 15 Year Old"]

for b in vault:
    if b in stock_list:
        inactive_bottles_list.remove(b)        
 

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

print("Please note that number might be higher because of included:\weird characters and metabase discrepancies (some bottles are actually active).")
