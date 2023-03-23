import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureMethod(self):
        print("I will be executed in fixture method1")

    def test_fixtureMethod2(self):
        print("I will be executed in fixture method2")

    def test_fixtureMethod3(self):
        print("I will be executed in fixture method3")

    def test_fixtureMethod4(self):
        print("I will be executed in fixture method4")
