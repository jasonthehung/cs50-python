def main():
    name = input("What's your name? ")

    if name.strip() == "":
        hello()
    else:
        hello(name.title())


def hello(to="world"):
    print("Hello,", to)


main()
