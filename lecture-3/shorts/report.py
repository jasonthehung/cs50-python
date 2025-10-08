def main():
    spacecraft = {"name": "Apollo 11", "distance": "384,400"}
    # Overwrite name and distance
    spacecraft.update({"name": "Voyager 1", "distance": "22,300,000,000"})
    spacecraft.update({"speed": "61,000"})  # Add speed
    report = create_report(spacecraft)
    print(report)


def create_report(spacecraft):
    return f"""
    ============= REPORT =============

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} km
    Speed: {spacecraft.get("speed", "Unknown")} km/h

    ==================================
    """


main()
