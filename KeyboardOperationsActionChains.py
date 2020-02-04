from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings/")
driver.find_element_by_name("fld_username").send_keys("Hello")

act=ActionChains(driver)
# act.send_keys(Keys.TAB).perform()
# time.sleep(5)
# # Combination method Special keys + Alphabet
act.key_down(Keys.CONTROL).send_keys('a').perform()


# I CAN NOT REPRODUCE #150