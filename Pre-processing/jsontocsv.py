import json
import csv

with open("./resources/demo.json") as file:
    data = json.load(file)
#News_Category_Dataset_v2.json
fname = "output.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file,lineterminator='\n')
    csv_file.writerow(["CATEGORY","HEADLINE","AUTHORS","LINK", "SHORT_DESCRIPTION", "DATE"])
    for item in data["root"]:
        csv_file.writerow([item['category'],item['headline'],item['authors'],item['link'], item['short_description'], item['date']])
