WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    remaining = 5

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Enter a word: ").upper().strip()
        remaining -= 1

        if guess in WORDS:
            print(f"Correct! You scored {WORDS[guess]} points!")
            del WORDS[guess]

        if remaining == 0:
            print("Out of guesses! Game over.")
            print(f"You missed: {', '.join(WORDS.keys())}")
            WORDS.clear()

    print("Congratulations! You found all the words!")


main()
