name = input("What's your name? ").strip().title()

match name:
    case "Jason" | "Jacky" | "Jackson":
        print("JJ")
    case "Ann":
        print("AA")
    case _:
        print("Who are U?")
