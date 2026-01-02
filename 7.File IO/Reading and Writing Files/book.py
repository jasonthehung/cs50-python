import os

CURR_FILE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(f"{CURR_FILE_DIR}/alice.txt", "r") as file:
        contents = file.readline()
        print(contents)


if __name__ == "__main__":
    main()
