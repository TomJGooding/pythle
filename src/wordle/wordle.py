from dataclasses import dataclass
import os
import pkgutil
import random
import sys


"""
WORD LISTS
"""


def load_wordlist(file_name: str) -> list[str]:
    text = pkgutil.get_data(__name__, "data/" + file_name).decode()
    word_list = text.splitlines()
    return word_list


WORDS = load_wordlist("words.txt")
SOLUTIONS = load_wordlist("solutions.txt")


"""
GAME LOGIC
"""
MAX_GUESSES = 6


@dataclass
class PlayerStats:
    games_played: int = 0
    wins: int = 0
    win_streak: int = 0

    def win_ratio(self) -> int:
        if self.games_played == 0:
            win_ratio = 0
        else:
            win_ratio = round((self.wins / self.games_played) * 100)
        return win_ratio


def guess_score(guess: str, solution: str) -> list[dict]:
    # Score player guess by assigning colour to letter/position
    guess_score = []
    for idx, char in enumerate(guess):
        if char not in solution:
            guess_score.append({char: "blue"})  # Not in word
        elif guess[idx] == solution[idx]:
            guess_score.append({char: "green"})  # Correct spot
        else:
            guess_score.append({char: "yellow"})  # In word but wrong spot

    return guess_score


"""
USER INTERFACE
"""


def display_title_art() -> None:
    print(
        """
 _ _ _ _____ _____ ____  __    _____
| | | |     | __  |    \\|  |  |   __|
| | | |  |  |    -|  |  |  |__|   __|
|_____|_____|__|__|____/|_____|_____|"""
    )


def display_player_stats(player_stats: PlayerStats) -> None:
    print(
        f"""
====================================
            STATISTICS
        {player_stats.games_played} Played, {player_stats.win_ratio()}% Wins
        Current Streak is {player_stats.win_streak}
====================================
"""
    )


def get_player_guess(word_list: list[str], guesses: list[str]) -> str:
    # Validates the player input from the user
    while True:
        print(f"Enter your guess ({len(guesses) + 1} / {MAX_GUESSES}), or 'Q' to quit.")
        guess = input()
        guess = guess.upper()
        if guess != "Q" and guess not in word_list:
            print("Each guess must be a valid five-letter word.")
        else:
            return guess


os.system("color")  # enables ANSI colors in Windows terminal
ansi_colours = {"green": "42", "yellow": "43", "blue": "44"}


def display_guess_score(guess_score: list[dict]) -> None:
    # Print the guess scores to the terminal, adding colout with ansi escape characters
    for letter_score in guess_score:
        for letter, colour in letter_score.items():
            print(f"\033[{ansi_colours[colour]}m {letter} \033[0;0m", end="")


def display_all_guess_scores(guesses: list[str], solution: str) -> None:
    # Print all guess scores to the terminal
    for guess in guesses:
        display_guess_score(guess_score(guess, solution))
        print("")  # Adds new line between guess score


"""
WORDLE GAME
"""


def main():
    player_stats = PlayerStats()

    while True:  # Main game loop
        solution: str = random.choice(SOLUTIONS)  # Set new solution
        guesses: list[str] = []  # Reset player guesses

        display_title_art()
        display_player_stats(player_stats)

        while len(guesses) < MAX_GUESSES:  # Loop for each player guess
            guess = get_player_guess(WORDS, guesses)
            if guess.upper() == "Q":
                print("Thanks for playing!\n")
                sys.exit()
            else:
                guesses.append(guess)
                display_all_guess_scores(guesses, solution)
                if guess == solution:
                    print("\nYou win!\n")
                    player_stats.games_played += 1
                    player_stats.wins += 1
                    player_stats.win_streak += 1
                    break
                if len(guesses) == MAX_GUESSES:
                    print(f"\nYou lose! The Wordle was {solution}.\n")
                    player_stats.games_played += 1
                    player_stats.win_streak = 0

        while True:  # Each guess loop
            print("Play again? Enter 'Y' to continue or 'N' to quit.")
            user_continue = input()
            if user_continue.upper() == "N":
                sys.exit("Thanks for playing!\n")  # Quit
            if user_continue.upper() == "Y":
                break


if __name__ == "__main__":
    main()
