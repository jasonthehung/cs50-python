import re


def main():
    email = input("Your email? ").strip()

    # [a-zA-Z0-9_] == \w
    print(validate_email(email))


def validate_email(email):
    return re.match(r"^(\w|\.)+@(\w+.)?\w+\.edu$", email, re.IGNORECASE)


if __name__ == "__main__":
    main()
