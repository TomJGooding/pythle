from pythle.player_stats import PlayerStats


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