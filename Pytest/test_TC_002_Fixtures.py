from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope="module") #Adding scope lets us reduce time and execute fixture (start and close browser) only once.
def setPath():
    global driver
    path = ("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
    driver = Chrome(executable_path=path)
    yield #Operator says what shoud do, after the test was execution
    driver.close()


def test_registration_valid_data(setPath):
    driver.get("http://www.theTestingWorld.com/Testing")
    driver.maximize_window()


def test_registration_invalid_data(setPath):
    driver.get("http://www.theTestingWorld.com/Testing")
    driver.maximize_window()


def test_invalid_data(setPath):
    driver.get("http://www.theTestingWorld.com/Testing")
    driver.maximize_window()