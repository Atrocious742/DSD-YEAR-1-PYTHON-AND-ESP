import csv

FILENAME = "scores.csv"

def add_score(username, score):
    """Add username+score to the CSV file and add header if file is empty."""

    try:
        with open(FILENAME, "r") as file:
            first_char = file.read(1)
    except FileNotFoundError:
        first_char = ""

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)

        if first_char == "":
            writer.writerow(["Username", "Score"])

        writer.writerow([username, score])


def show_scores():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No scores found yet.")


def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")

            while True:
                try:
                    score = int(input("Enter score (0–100): "))
                    if 0 <= score <= 100:
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

            add_score(username, score)

        elif choice == "2":
            show_scores()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()