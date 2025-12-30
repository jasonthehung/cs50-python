from random import choice, randint, shuffle


def trial():
    counts = 0
    flips = 0
    while counts < 10:
        coin = choice(["heads", "tails"])
        flips += 1
        if coin == "heads":
            counts += 1
        else:
            counts = 0
    return flips


runs = 10000
# avg = sum(trial() for _ in range(runs)) / runs
# print(avg)


print(randint(10, 20))

cards = ["jack", "queen", "king"]
shuffle(cards)
print(cards)
