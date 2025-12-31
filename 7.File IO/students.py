import csv
import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))
students_file = f"{current_file_dir}/students.csv"

name = input("What's your name? ")
house = input("What's your house? ")

with open(students_file, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"house": house, "name": name})


students = []
with open(students_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)


for std in sorted(students, key=lambda std: std["name"], reverse=False):
    print(f"{std["name"]} is in {std["house"]}")
