import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield  # post request
    print("I will be executed last")


def test_fixtureMethod(setup):
    print("I will be executed in fixture method")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
