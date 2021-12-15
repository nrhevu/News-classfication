import json
import csv
from xxx import preprocess

with open('./Pre-processing/resources/News_Category_Dataset_v2.json') as file:
    data = json.load(file)

#News_Category_Dataset_v2.json
fname = "Pre-processing/output.csv"

with open(fname, "w", encoding="utf-8") as file:
    csv_file = csv.writer(file,lineterminator='\n')
    csv_file.writerow(["CATEGORY","HEADLINE"])
    for item in data["root"]:
        csv_file.writerow([item['category'], preprocess(item['headline'])])
