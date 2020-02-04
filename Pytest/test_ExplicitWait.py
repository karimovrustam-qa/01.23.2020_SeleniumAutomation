from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait # Import for Explicit Waits
from selenium.webdriver.common.by import By # Import for Explicit Waits
import selenium.webdriver.support.expected_conditions as ec # Import for Explicit Waits
import pytest
import time

@pytest.fixture()
def environment_setup():
    global driver
    path = "/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.refresh()
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    wait=WebDriverWait(driver,4) # Wait for a certain condition to occur before proceeding further in the code (for example, 4 sec)

    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),'India')) # Example explicit wait
    object=Select(driver.find_element_by_id("countryId"))
    object.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), 'Delhi')) # Example explicit wait
    object = Select(driver.find_element_by_id("stateId"))
    object.select_by_visible_text("Delhi")
