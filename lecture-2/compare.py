def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("X is Even")
    else:
        print("X is Odd")


def is_even(value):
    return value % 2 == 0


main()
