import pytest


@pytest.fixture
def order():
    return []


def test_order(order):
    assert order == [1, 2, 3]


# When a test is marked as having an error, it doesn’t mean the test failed, though.
# It just means the test couldn’t even be attempted because one of the things it depends on had a problem.
