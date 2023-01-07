import pytest


@pytest.fixture()
def setup():
    print("Browser Launch")


def test_case1():
    print("Test case 1 complete")


def test_case2():
    print("Test case 2 complete")
