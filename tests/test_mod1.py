from mod1 import add


def test_add() -> None:
    assert add(1, 2) == 3


def test_add_unhappy() -> None:
    assert add(1, 2) == 5
