import sys

if len(sys.argv) < 2:
    sys.exit("Too few args")
elif len(sys.argv) > 2:
    sys.exit("Too many args")


print(f"Hello, my name is {sys.argv[1]}")
