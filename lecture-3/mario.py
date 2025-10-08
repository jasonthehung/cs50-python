def main():
    print_column(3)

    print()

    print_square(3)


def print_column(height):
    for i in range(height):
        print("#")


def print_square(size):
    for i in range(size):
        print("#" * size)


main()
