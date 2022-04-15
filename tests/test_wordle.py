from wordle.wordle import player_stats_str, guess_count_str, guess_score


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


print(guess_score("ABCDE", "EDCBA"))
