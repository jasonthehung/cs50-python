distances = {
    "Voyager 1": 22_000_000_000,  # in kilometers
    "Apollo 11": 384_400,         # in kilometers
    "ISS": 408,                   # in kilometers
    "Mars Rover": 225_000_000,    # in kilometers
}


def main():
    for name in distances:
        distance = distances[name]
        print(f"{name} is {distance:,} km away.")


main()
