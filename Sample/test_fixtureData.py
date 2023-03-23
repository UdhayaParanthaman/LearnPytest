import pytest


@pytest.mark.usefixtures("loadData")
class TestDatadriver:

    def test_editprofile(self,loadData):
        print("data load successfully")
        print(loadData)
        print(loadData[0])
        print(loadData[1])

    def test_crossBrowser(self,crossBrowser):
        print(crossBrowser)

