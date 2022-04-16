import os
import pkgutil
import random
import sys


def load_wordlist(file_name: str) -> list[str]:
    text = pkgutil.get_data(__name__, "data/" + file_name).decode()
    word_list = text.splitlines()
    return word_list


WORDS = load_wordlist("words.txt")
SOLUTIONS = load_wordlist("solutions.txt")

GAME_TITLE_ART = """
 _ _ _ _____ _____ ____  __    _____
| | | |     | __  |    \|  |  |   __|
| | | |  |  |    -|  |  |  |__|   __|
|_____|_____|__|__|____/|_____|_____|"""


MAX_GUESSES = 6


def main():
    # Track player statistics
    games_played = 0
    wins = 0
    win_streak = 0

    while True:  # Main game loop
        solution = random.choice(SOLUTIONS)

        print(GAME_TITLE_ART)
        print(player_stats_str(games_played, wins, win_streak))

        guesses = []

        while True:  # Each guess loop
            while True:  # Player input loop
                print(f"Enter your guess {guess_count_str(guesses)}, or 'Q' to quit.")
                guess = input()
                if guess.upper() == "Q":
                    sys.exit("Thanks for playing!\n")  # Quit
                elif guess.upper() not in WORDS:
                    print("Each guess must be a valid five-letter word.")
                else:
                    break
            guesses.append(guess.upper())
            print_all_guesses(guesses, solution)
            if guess.upper() == solution:
                print("\nYou win!\n")
                games_played += 1
                wins += 1
                win_streak += 1
                break
            if len(guesses) == MAX_GUESSES:
                print(f"\nYou lose! The Wordle was {solution}.\n")
                games_played += 1
                win_streak = 0
                break
        while True:  # Each guess loop
            print("Play again? Enter 'Y' to continue or 'N' to quit.")
            user_continue = input()
            if user_continue.upper() == "N":
                sys.exit("Thanks for playing!\n")  # Quit
            if user_continue.upper() == "Y":
                break


def player_stats_str(games_played: int, wins: int, win_streak: int) -> str:
    if games_played != 0:
        win_ratio = round((wins / games_played) * 100)
    else:
        win_ratio = 0
    return f"""
====================================
            STATISTICS
        {games_played} Played, {win_ratio}% Wins
        Current Streak is {win_streak}
====================================
"""


def guess_count_str(guesses: list[str]) -> str:
    guess_count = len(guesses) + 1
    return f"({guess_count} / {MAX_GUESSES})"


os.system("color")  # enables ansi escape characters in terminal

# Assign Wordle colours to ANSI colour numbers,
ansi_colours = {"green": "42", "yellow": "43", "blue": "44"}


def guess_score(guess: str, solution: str) -> list[dict]:
    # Score player guess by assigning colour to letter/position
    guess_score = []
    for idx, char in enumerate(guess):
        if char not in solution:
            guess_score.append({char: "blue"})
        elif guess[idx] == solution[idx]:
            guess_score.append({char: "green"})
        else:
            guess_score.append({char: "yellow"})

    return guess_score


def print_guess_score(guess_score: list[dict]) -> None:
    # Print the guess scores to the terminal, adding colout with ansi escape characters
    for letter_score in guess_score:
        for letter, colour in letter_score.items():
            print(f"\033[{ansi_colours[colour]}m {letter} \033[0;0m", end="")


def print_all_guesses(guesses: list[str], solution: str) -> None:
    # Print all guess scores to the terminal
    for guess in guesses:
        print_guess_score(guess_score(guess, solution))
        print("")  # Adds new line between guess score


if __name__ == "__main__":
    main()
