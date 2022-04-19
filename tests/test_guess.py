from pythle.guess import Guess


def test_guess_score():
    assert Guess.guess_score("AAAAA", "AAAAA") == [
        {"A": "green"},
        {"A": "green"},
        {"A": "green"},
        {"A": "green"},
        {"A": "green"},
    ]
    assert Guess.guess_score("AAAAA", "ZZZZZ") == [
        {"A": "blue"},
        {"A": "blue"},
        {"A": "blue"},
        {"A": "blue"},
        {"A": "blue"},
    ]
    assert Guess.guess_score("ABCDE", "EDCBA") == [
        {"A": "yellow"},
        {"B": "yellow"},
        {"C": "green"},
        {"D": "yellow"},
        {"E": "yellow"},
    ]
