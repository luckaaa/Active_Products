Active Products Bot - Flaviar

1.

	1. Setup active_products.csv file ---> for up to date information download it here: 

	https://metabase.flaviar.com/question#eyJuYW1lIjoiU1dFREVOIiwiZGVzY3JpcHRpb24iOm51bGwsImRhdGFzZXRfcXVlcnkiOnsidHlwZSI6InF1ZXJ5IiwicXVlcnkiOnsic291cmNlLXRhYmxlIjo3NjAsImZpbHRlciI6WyJhbmQiLFsiPSIsWyJmaWVsZCIsMzc5LHsic291cmNlLWZpZWxkIjoxODA2NywidGVtcG9yYWwtdW5pdCI6ImRheSJ9XSwiMjAyMi0wMS0wM1QwMDowMDowMFoiXSxbIj0iLFsiZmllbGQiLDE4MDY5LG51bGxdLCJCb3R0bGUiXSxbIj0iLFsiZmllbGQiLDE4MDY0LG51bGxdLCJTTE9WRU5JQSJdXX0sImRhdGFiYXNlIjoyfSwiZGlzcGxheSI6InRhYmxlIiwiZGlzcGxheUlzTG9ja2VkIjp0cnVlLCJ2aXN1YWxpemF0aW9uX3NldHRpbmdzIjp7InBpdm90X3RhYmxlLmNvbHVtbl9zcGxpdCI6eyJyb3dzIjpbWyJmaWVsZCIsMTgwNjQsbnVsbF0sWyJmaWVsZCIsMTgwNjksbnVsbF1dLCJjb2x1bW5zIjpbWyJmaWVsZCIsMzc5LHsidGVtcG9yYWwtdW5pdCI6ImRheSIsInNvdXJjZS1maWVsZCI6MTgwNjd9XV0sInZhbHVlcyI6W1siYWdncmVnYXRpb24iLDBdXX0sImdyYXBoLmRpbWVuc2lvbnMiOlsiZGF0ZSIsImdlb2xvY2F0aW9uX25hbWUiXSwiZ3JhcGgubWV0cmljcyI6WyJjb3VudCJdfSwib3JpZ2luYWxfY2FyZF9pZCI6Mjk4N30=

	2. Must be downloaded and saved as active_products.csv. Put it in the same folder where main.py file lives!



2.

	1. wms.flaviar.com/inventory -> Only On Stock must be ticked, Product Type = bottle only.
	2. Export stock.csv and save in the file alongside active_products.csv and main.py.
	3. Open stock.csv and remove duplicates by ID.
	4. Select B column without the "Title" row -> Text to Columns ->	Delimited (next) -> Other and type in "-" without the quotation marks (next) -> tick Do not import column -> Finish
	5. Again click Text to Columns -> Fixed width (next) -> Click on the first little line on scale - 1/100 (next) -> Do not import column (skip) -> Finish
	6. Save file.


3.

	1. Open main.py with your text editor (I prefer PyCharm)
	2. Open terminal and install pandas -> pip install pandas
	3. Run the code.


4. Please note that number might be higher because of included: 
	tasting samples,
	weird characters,
	metabase discrepancies (some bottles are actually active)
