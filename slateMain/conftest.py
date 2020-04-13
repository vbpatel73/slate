import pytest
from selenium import webdriver as wd

def pytest_addoption(parser):
    parser.addoption("--b", action="store", default="chrome", help="my option: browser"   )



@pytest.fixture(scope="session")
def getBrowser(request):		
	x = request.config.getoption("--b")
	return x
	
