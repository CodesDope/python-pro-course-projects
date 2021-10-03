import csv

with open("new_file.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["roll_no", "name", "marks"])
    writer.writerow({"roll_no": 1, "name": "Tony", "marks": 650})
    writer.writerow({"roll_no": 2, "name": "Bruce", "marks": 600})
