from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com")
act=ActionChains(driver)
# driver.find_element_by_xpath("//a[text()='Login']")

# Click operations (left click)
# act.click().perform()
# act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Context click (right click)
# act.context_click().perform()
# act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Click operations (double click)
# act.double_click().perform()
# act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Moving mouse
act.move_to_element(driver.find_element_by_xpath("//span[text()='TUTORIAL ']")).perform()
# or
# act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()