import re


def main():
    name = input("Name: ").strip()
    print(format_name(name))


def format_name(name):
    if matches := re.search(r"^(.+) *, *(.+)$", name):
        name = f"{matches.group(2)} {matches.group(1)}"

    return name


if __name__ == "__main__":
    main()
