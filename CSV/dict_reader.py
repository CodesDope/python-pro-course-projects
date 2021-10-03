import csv

with open("student_marks.csv", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # print(row)
        roll_no = row["roll_no"]
        name = row["name"]
        marks = row["marks"]
        print(f"Roll No.: {roll_no}\tName: {name}\tMarks: {marks}")


with open("student_marks.csv", newline="") as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=["a", "b", "c"])
    for row in reader:
        # print(row)
        roll_no = row["a"]
        name = row["a"]
        marks = row["c"]
        print(f"Roll No.: {roll_no}\tName: {name}\tMarks: {marks}")
