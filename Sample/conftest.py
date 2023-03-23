import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield  # post request
    print("I will be executed last")


@pytest.fixture()
def loadData():
    print("profile data is being executed")
    return ["Udhaya", "Kumar"]


@pytest.fixture(params=[("chrome","Udhaya"), ("Firefox","Kumar"), "Edge", "IE"])
def crossBrowser(request):
    return request.param
