import csv

with open("new_file.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([1, "Tony", 650])
    writer.writerow([2, "Bruce", 600])

with open("new_file.csv", "a", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([3, "Steve", 500])


with open("new_file_2.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow([1, "Tony", 650])
    writer.writerow([2, "Bruce", 600])
