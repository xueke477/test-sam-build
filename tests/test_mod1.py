from mod1 import add
import pytest
from pytest_mock import MockerFixture


@pytest.fixture
def one():
    return 1


def test_add(one) -> None:
    assert add(one, 2) == 3


def test_add_happy(mocker) -> None:
    mocked_fcn = mocker.patch('test_mod1.add')
    mocked_fcn.return_value = 5
    assert add(1, 3) == 5


def test_add_happy2() -> None:
    assert add(1, 4) == 5


def test_add_happy3() -> None:
    assert add(1, 4) == 5


def test_add_happy4() -> None:
    assert add(1, 4) == 5
