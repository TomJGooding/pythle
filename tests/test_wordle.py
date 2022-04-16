from wordle.wordle import (
    guess_score,
    display_guess_score,
    display_all_guess_scores,
    display_title_art,
    PlayerStats,
    display_player_stats,
)

"""
GAME LOGIC TESTS
"""


def test_playerstats_default_values():
    player_stats = PlayerStats()
    assert player_stats.games_played == 0
    assert player_stats.wins == 0
    assert player_stats.win_streak == 0


def test_playerstats_add_values():
    player_stats = PlayerStats(3, 2, 1)
    assert player_stats.games_played == 3
    assert player_stats.wins == 2
    assert player_stats.win_streak == 1


def test_playerstats_win_ratio_when_zero_games_played():
    player_stats = PlayerStats()
    assert player_stats.win_ratio() == 0


def test_playerstats_win_ratio():
    player_stats = PlayerStats(4, 2, 0)
    assert player_stats.win_ratio() == 50


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


"""
USER INTERFACE TESTS
"""


def test_display_title_art(capfd):
    display_title_art()
    out, err = capfd.readouterr()
    assert (
        out
        == """
 _ _ _ _____ _____ ____  __    _____
| | | |     | __  |    \\|  |  |   __|
| | | |  |  |    -|  |  |  |__|   __|
|_____|_____|__|__|____/|_____|_____|
"""
    )


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


def test_display_guess_score(capfd):
    display_guess_score(
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


def test_display_all_guess_scores(capfd):
    display_all_guess_scores(["AAAAA", "BBBBB"], "ZZZZZ")
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
