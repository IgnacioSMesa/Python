import csv

with open("hollow_knight.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)