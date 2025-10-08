# ["Mario", "Luigi"]
results = ["Mario", "Luigi"]

# ["Mario", "Luigi", "Yoshi"]
results.append("Yoshi")

# ["Mario", "Luigi", "Yoshi", "Toad", "Princess"]
results.extend(["Toad", "Princess"])

# ["Mario", "Luigi", "Yoshi", "Princess"]
results.remove("Toad")

# ["Mario", "Bowser", "Luigi", "Yoshi", "Princess"]
results.insert(1, "Bowser")

# ["Princess", "Yoshi", "Luigi", "Bowser", "Mario"]
results.reverse()

print(results)
