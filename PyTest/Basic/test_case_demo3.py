import pytest


@pytest.fixture()
def setup():
    print("Browser Launch")
    yield
    print("Browser Closed")


@pytest.mark.order(2)
def test_case1(setup):
    print("Test case 1 complete")


@pytest.mark.order(1)
def test_case2(setup):
    print("Test case 2 complete")


@pytest.mark.order(4)
def test_case3(setup):
    print("Test case 3 complete")


@pytest.mark.order(3)
def test_case4(setup):
    print("Test case 4 complete")
