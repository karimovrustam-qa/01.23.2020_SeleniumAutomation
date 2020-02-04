from selenium.webdriver import Chrome
import pytest

# Test Case file name ALWAYS starts with "test"
# Test Case method name ALWAYS starts with "test"
# If you have issues with running: go to Menu->Run->Edit_Configurations, then copy name
# and interpreter, add to "Python Tests", add name, interpreter and working directory
# and remove from "Python". Able to run through the Terminal
#
# a=101
#
# @pytest.mark.skip("Don't want to execute in current build") # necessary import pytest
# or
# @pytest.mark.skipif(a>100,reason="Down") # Condition - skip execution
# or
# using terminal -> pytest -k test_registration_invalid_data
# or
# using terminal write word which you have in tests, which must be execute -> pytest -k registration


@pytest.mark.Smoke #Grouping Test Case
def test_registration_valid_data():
    path=("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
    driver=Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/Testing")
    driver.maximize_window()

@pytest.mark.Sanity #Grouping Test Case
def test_registration_invalid_data():
    path=("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
    driver=Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/Testing")
    driver.maximize_window()

@pytest.mark.Smoke #Grouping Test Case
def test_invalid_data():
    path=("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
    driver=Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/Testing")
    driver.maximize_window()


