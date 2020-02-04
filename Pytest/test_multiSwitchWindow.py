from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "../drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys("test")
    driver.find_element_by_name("_txtPassword").send_keys("test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
    driver.find_element_by_xpath("//a[contains(text(),' My Account')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()
    time.sleep(10)
    allwindows=driver.window_handles # Gives information about current windows
    print(allwindows)

    # Method lets get URL of windows, using in this case
    # for win in allwindows: # Using LOOP for picking unique value in each windows
    #     driver.switch_to.window(win) # That switching to that picked up windows
    #     print(driver.current_url) # Print windows

    mainWin = ""
    for win in allwindows:
        driver.switch_to.window(win)
        if (driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element_by_xpath("//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif (driver.current_url=='https://www.thetestingworld.com/testings/dashboard.php'):
            mainWin=win

    driver.switch_to.window(mainWin)
    print(driver.current_url)


