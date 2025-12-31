import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))
students_file = f"{current_file_dir}/students.csv"

students = []

with open(students_file, "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        std = {"name": name, "house": house}

        students.append(std)


def get_name(std):
    return std["name"]


def get_house(std):
    return std["house"]


for std in sorted(students, key=get_house, reverse=True):
    print(f"{std["name"]} is in {std["house"]}")
