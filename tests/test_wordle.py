from wordle.wordle import (
    player_stats_str,
    guess_count_str,
    guess_score,
    print_guess_score,
    print_all_guesses,
)


def test_player_stats_str():
    assert (
        player_stats_str(0, 0, 0)
        == """
====================================
            STATISTICS
        0 Played, 0% Wins
        Current Streak is 0
====================================
"""
    )
    assert (
        player_stats_str(2, 1, 0)
        == """
====================================
            STATISTICS
        2 Played, 50% Wins
        Current Streak is 0
====================================
"""
    )
    assert (
        player_stats_str(5, 5, 5)
        == """
====================================
            STATISTICS
        5 Played, 100% Wins
        Current Streak is 5
====================================
"""
    )


def test_guess_count_str():
    assert guess_count_str([]) == "(1 / 6)"
    assert guess_count_str(["WORDS"]) == "(2 / 6)"
    assert guess_count_str(["WORDS", "WORDS", "WORDS", "WORDS", "WORDS"]) == "(6 / 6)"


def test_guess_score():
    assert guess_score("AAAAA", "AAAAA") == [
        {"A": "green"},
        {"A": "green"},
        {"A": "green"},
        {"A": "green"},
        {"A": "green"},
    ]
    assert guess_score("AAAAA", "ZZZZZ") == [
        {"A": "blue"},
        {"A": "blue"},
        {"A": "blue"},
        {"A": "blue"},
        {"A": "blue"},
    ]
    assert guess_score("ABCDE", "EDCBA") == [
        {"A": "yellow"},
        {"B": "yellow"},
        {"C": "green"},
        {"D": "yellow"},
        {"E": "yellow"},
    ]


def test_print_guess_score(capfd):
    print_guess_score(
        [{"A": "green"}, {"A": "green"}, {"A": "green"}, {"A": "green"}, {"A": "green"}]
    )
    out, err = capfd.readouterr()
    assert (
        out
        == "\033[42m A \033[0;0m"
        + "\033[42m A \033[0;0m"
        + "\033[42m A \033[0;0m"
        + "\033[42m A \033[0;0m"
        + "\033[42m A \033[0;0m"
    )


def test_print_all_guesses(capfd):
    print_all_guesses(["AAAAA", "BBBBB"], "ZZZZZ")
    out, err = capfd.readouterr()
    assert (
        out
        == "\033[44m A \033[0;0m"
        + "\033[44m A \033[0;0m"
        + "\033[44m A \033[0;0m"
        + "\033[44m A \033[0;0m"
        + "\033[44m A \033[0;0m"
        + "\n"
        + "\033[44m B \033[0;0m"
        + "\033[44m B \033[0;0m"
        + "\033[44m B \033[0;0m"
        + "\033[44m B \033[0;0m"
        + "\033[44m B \033[0;0m"
        + "\n"
    )
