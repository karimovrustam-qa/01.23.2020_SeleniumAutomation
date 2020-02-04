from selenium.webdriver import Chrome
import ScreenMethod

# Base code
# path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
# driver=Chrome(executable_path=path)
# driver.maximize_window()
# driver.get('https://translate.google.com/')
#
# driver.get_screenshot_as_file('/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/ScreenShots/new.png')
#
# driver.close()
# quit()

# Code with def method from ScreenMethod.py
path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver=Chrome(executable_path=path)
driver.maximize_window()
driver.get('https://www.thetestingworld.com/testings/')

ScreenMethod.make_page_screenshot(driver,"First_Screenshot") # Using external method def

driver.close()
quit()
