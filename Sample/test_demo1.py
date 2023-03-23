# Any pytest starts with test_ or end with _test
import pytest


# pytest standards define the code in Functions
# In pytest method name always starts with test keyword

# if we have same method name in pytest, will override
def test_firstProgram():
    print("Hello Test")


def test_secondProgram():
    print("Welcome to Python Pytest Framework")


@pytest.mark.card
def test_creditCard():
    msg = "Hello"
    assert msg == "Hi"
    print("executed")
