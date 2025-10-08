# dict

stds = [
    {"name": "Hermion", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for std in stds:
    print(
        f"{std["name"]} lives in {std["house"]} and their patronus is {std["patronus"]}"
    )
