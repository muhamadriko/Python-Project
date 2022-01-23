import csv
import requests
response = requests.get("https://api.abcfdab.cfd/students/")
data = response.json()
datafix = data['data']

keys = datafix[0].keys()
 
with open("tbl_students_0143.csv", "w") as file:
 csvwriter = csv.DictWriter(file, keys)
 csvwriter.writeheader()
 csvwriter.writerows(datafix)
