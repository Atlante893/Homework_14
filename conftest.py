import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def chrome_web_test():
    driver_chrome = webdriver.Chrome(ChromeDriverManager().install())
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def firefox_web_test():
    driver_firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield driver_firefox
    driver_firefox.quit()


@pytest.fixture()
def edge_web_test():
    driver_edge = webdriver.Edge(EdgeChromiumDriverManager().install())
    yield driver_edge
    driver_edge.quit()