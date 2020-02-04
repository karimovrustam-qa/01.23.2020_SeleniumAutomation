from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest
import time

@pytest.fixture()
def environment_setup():
    global driver
    path = "/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.set_page_load_timeout(30) #Wait necessary time, until the web-page will load
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    object=Select(driver.find_element_by_name("sex"))
    object.select_by_visible_text("Male")

    time.sleep(20) #When we exactly know - how much time wait

    driver.find_element_by_xpath("//input[@value='office']").click()

    object=Select(driver.find_element_by_name("sex"))
    object.select_by_visible_text("Male")

    driver.find_element_by_xpath("//input[@name='terms']").click()
    driver.find_element_by_xpath("//input[@type='submit']").click()
    driver.find_element_by_link_text("Read Detail").click()

    assert driver.current_url == "https://www.thetestingworld.com/testings/"