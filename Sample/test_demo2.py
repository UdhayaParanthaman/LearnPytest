# Any pytest starts with test_ or end with _test
import pytest


# pytest standards define the code in Functions
# In pytest method name always starts with test keyword
def test_firstProgram():
    print("Hello Test")


def test_firstProgram():
    print("Good Morning")


# if we have same method name in pytest, will override
@pytest.mark.card
def test_firstProgram(setup):
    print("Good Morning Pytest")


@pytest.mark.skip
def test_secondProgram():
    print("Welcome to Python Pytest Framework")



