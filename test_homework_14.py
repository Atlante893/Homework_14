from selenium.webdriver.common.by import By
import time


def test_chrome(chrome_web_test):
    user_email = "eshenko.poul@gmail.com"
    user_password = "123456"
    driver_chrome = chrome_web_test
    driver_chrome.maximize_window()
    driver_chrome.get("https://app.memrise.com/signin")
    time.sleep(3)
    email_input_locator = "//input[@id='username']"
    email_input_element = driver_chrome.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_email)
    password_input_id = "password"
    password_input_element = driver_chrome.find_element(By.ID, password_input_id)
    password_input_element.clear()
    password_input_element.send_keys(user_password)
    login_button_locator = "//button[@type='submit']"
    login_button_element = driver_chrome.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    time.sleep(3)
    current_title = driver_chrome.title
    assert current_title == "Memrise", f'\nActual:{current_title}\nExpected: "Memrise"'


def test_firefox(firefox_web_test):
    user_email = "eshenko.poul@gmail.com"
    user_password = "123456"
    driver_firefox = firefox_web_test
    driver_firefox.maximize_window()
    driver_firefox.get("https://app.memrise.com/signin")
    time.sleep(3)
    email_input_locator = "//input[@id='username']"
    email_input_element = driver_firefox.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_email)
    password_input_id = "password"
    password_input_element = driver_firefox.find_element(By.ID, password_input_id)
    password_input_element.clear()
    password_input_element.send_keys(user_password)
    login_button_locator = "//button[@type='submit']"
    login_button_element = driver_firefox.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    time.sleep(3)
    current_title = driver_firefox.title
    assert current_title == "Memrise", f'\nActual:{current_title}\nExpected: "Memrise"'


def test_edge(edge_web_test):
    user_email = "eshenko.poul@gmail.com"
    user_password = "123456"
    driver_edge = edge_web_test
    driver_edge.maximize_window()
    driver_edge.get("https://app.memrise.com/signin")
    time.sleep(3)
    email_input_locator = "//input[@id='username']"
    email_input_element = driver_edge.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_email)
    password_input_id = "password"
    password_input_element = driver_edge.find_element(By.ID, password_input_id)
    password_input_element.clear()
    password_input_element.send_keys(user_password)
    login_button_locator = "//button[@type='submit']"
    login_button_element = driver_edge.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    time.sleep(3)
    current_title = driver_edge.title
    assert current_title == "Memrise", f'\nActual:{current_title}\nExpected: "Memrise"'
