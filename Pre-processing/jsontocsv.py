import json
import csv
from xxx import preprocess, combine_text

with open('./Pre-processing/resources/News_Category_Dataset_v2.json') as file:
    data = json.load(file)

#News_Category_Dataset_v2.json
fname = "Pre-processing/output.csv"

with open(fname, "w", encoding="utf-8") as file:
    csv_file = csv.writer(file,lineterminator='\n')
    csv_file.writerow(["CATEGORY","CONTENT"])
    for item in data["root"]:
        content = []
        content.append(item['headline'])
        content.append(item['short_description'])
        content[0] = preprocess(content[0])
        content[1] = preprocess(content[1])
        txt = combine_text(content)
        csv_file.writerow([item['category'], txt])
