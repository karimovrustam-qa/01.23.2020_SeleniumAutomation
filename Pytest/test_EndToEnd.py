from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    object=Select(driver.find_element_by_name("sex"))
    object.select_by_visible_text("Male")

    driver.find_element_by_xpath("//input[@value='office']").click()

    object=Select(driver.find_element_by_name("sex"))
    object.select_by_visible_text("Male")

    driver.find_element_by_xpath("//input[@name='terms']").click()
    driver.find_element_by_xpath("//input[@type='submit']").click()
    driver.find_element_by_link_text("Read Detail").click()

    assert driver.current_url == "https://www.thetestingworld.com/testings/"