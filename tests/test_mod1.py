from mod1 import add


def test_add() -> None:
    assert add(1, 2) == 3


def test_add_happy() -> None:
    assert add(1, 3) == 4


def test_add_happy2() -> None:
    assert add(1, 4) == 5


def test_add_happy3() -> None:
    assert add(1, 4) == 5


def test_add_happy4() -> None:
    assert add(1, 4) == 5
