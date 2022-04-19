from pythle.cli import (display_all_guess_scores, display_guess_score,
                        display_player_stats, display_title_art,
                        goodbye_message, lose_message, win_message)
from pythle.player_stats import PlayerStats


""" DISPLAY SCORE COLOURS TESTS """


def test_display_guess_score(capfd):
    display_guess_score([{"G": "green"}, {"Y": "yellow"}, {"B": "blue"}])
    out, err = capfd.readouterr()
    assert (
        out == "\033[42m G \033[0;0m" + "\033[43m Y \033[0;0m" + "\033[44m B \033[0;0m"
    )


def test_display_all_guess_scores(capfd):
    display_all_guess_scores(["ZZZ", "CBA", "ABC"], "ABC")
    out, err = capfd.readouterr()
    assert (
        out
        == "\033[44m Z \033[0;0m"
        + "\033[44m Z \033[0;0m"
        + "\033[44m Z \033[0;0m"
        + "\n"
        + "\033[43m C \033[0;0m"
        + "\033[42m B \033[0;0m"
        + "\033[43m A \033[0;0m"
        + "\n"
        + "\033[42m A \033[0;0m"
        + "\033[42m B \033[0;0m"
        + "\033[42m C \033[0;0m"
        + "\n"
    )


""" GET PLAYER INPUTS TESTS """


""" DISPLAY STATISTICS TESTS """


def test_display_player_stats(capfd):
    player_stats = PlayerStats(4, 2, 1)
    display_player_stats(player_stats)
    out, err = capfd.readouterr()
    assert (
        out
        == """
====================================
            STATISTICS
        4 Played, 50% Wins
        Current Streak is 1
====================================

"""
    )


""" OTHER MESSAGES """


def test_display_title_art(capfd):
    display_title_art()
    out, err = capfd.readouterr()
    assert (
        out
        == """
 _____ __ __ _____ _____ __    _____
|  _  |  |  |_   _|  |  |  |  |   __|
|   __|_   _| | | |     |  |__|   __|
|__|    |_|   |_| |__|__|_____|_____|
"""
    )


def test_goodbye_message(capfd):
    goodbye_message()
    out, err = capfd.readouterr()
    assert out == "Thanks for playing!\n\n"


def test_win_message(capfd):
    win_message()
    out, err = capfd.readouterr()
    assert out == "\nYou win!\n\n"


def test_lose_message(capfd):
    lose_message("APPLE")
    out, err = capfd.readouterr()
    assert out == "\nYou lose! The Wordle was APPLE.\n\n"
