import os

name = input("What's your name? ")

current_file_dir = os.path.dirname(os.path.abspath(__file__))
names_file = f"{current_file_dir}/names.txt"


with open(names_file, "a") as file:
    file.write(f"{name}\n")


with open(names_file, "r") as file:
    for line in sorted(file):
        print(line.rstrip())
