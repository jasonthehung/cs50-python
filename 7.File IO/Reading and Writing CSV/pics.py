import csv
import os

import numpy as np
from PIL import Image

CURR_FILE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(f"{CURR_FILE_DIR}/pics.csv", "r") as file, open(
        f"{CURR_FILE_DIR}/analysis.csv", "w", newline=""
    ) as analysis:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = calculate_brightness(f"{CURR_FILE_DIR}/{row["id"]}.png")
            writer.writerow(row)


def calculate_brightness(filename, r=2):
    with Image.open(filename) as img:
        brightness = round((np.mean(np.array(img.convert("L"))) / 255), r)
    return brightness


if __name__ == "__main__":
    main()
