from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope="module")
def setPath():
    global driver
    path = ("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
    driver = Chrome(executable_path=path)
    yield
    driver.close()


def test_registration_valid_data(setPath):
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms" #Assertions use when need to compare actual and expected result


def test_registration_invalid_data(setPath):
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    assert driver.current_url == "https://www.thetestingworld.com/testings/"


def test_invalid_data(setPath):
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()