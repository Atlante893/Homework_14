import pytest
from selenium.webdriver import Chrome, Edge, Firefox


@pytest.fixture()
def chrome_web_test():
    driver_chrome = Chrome("Drivers/chromedriver.exe")
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def firefox_web_test():
    driver_firefox = Firefox("Drivers/geckodriver.exe")
    yield driver_firefox
    driver_firefox.quit()


@pytest.fixture()
def edge_web_test():
    driver_edge = Edge("Drivers/msedgedriver.exe")
    yield driver_edge
    driver_edge.quit()