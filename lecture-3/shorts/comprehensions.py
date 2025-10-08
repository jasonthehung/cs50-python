import csv
import os


def main():
    words = get_words("plaintext.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 6]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    print(counts)

    save_counts(counts)


def get_words(filepath):
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    return text.split()


def save_counts(counts):
    with open("word_counts.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "counts"])
        for word, count in counts.items():
            writer.writerow([word, count])


main()
