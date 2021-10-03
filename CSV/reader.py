import csv

with open("student_marks.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    for index, row in enumerate(reader):
        if index == 0:
            continue
        # print(row)
        roll_no = row[0]
        name = row[1]
        marks = row[2]
        print(f"Roll No.: {roll_no}\tName: {name}\tMarks: {marks}")


with open("student_marks_2.csv", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    for index, row in enumerate(reader):
        if index == 0:
            continue
        # print(row)
        roll_no = row[0]
        name = row[1]
        marks = row[2]
        print(f"Roll No.: {roll_no}\tName: {name}\tMarks: {marks}")
