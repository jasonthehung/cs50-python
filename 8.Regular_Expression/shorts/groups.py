import re

locations = {"+1": "US", "+886": "Taiwan"}


def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    if match := re.search(pattern, number):
        print(locations[match.group("country_code")])
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
