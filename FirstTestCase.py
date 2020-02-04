import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select # Required when work with Dropdown or List


path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

driver.maximize_window()

driver.find_element_by_name("fld_username").send_keys("helloworld")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("mario@world.com")
driver.find_element_by_name("fld_password").send_keys("abcd123")
driver.find_element_by_name("fld_cpassword").send_keys("abcd123")
# We can change the value which were added previously in the field
driver.find_element_by_name("fld_username").clear()
driver.find_element_by_name("fld_username").send_keys("abcd123")
# Working for radio button
driver.find_element_by_xpath("//input[@value='office']").click()

# ATTENTION! Working on Dropdown (when choose only one value) and List (when choose more then one value)
object=Select(driver.find_element_by_name("sex"))
# First Method
# object.select_by_index(2)
# Second Method
# object.select_by_value("2")
# Third Method
object.select_by_visible_text("Male")

# ATTENTION! Working ONLY on List
# This method works when you need deselect values from the list. Example: you selected 4 values, and
# you need deselect 2 of them, for this one you can use deselected my any methods.
# object.deselect_by_index(2)

# Working for checkbox
driver.find_element_by_xpath("//input[@name='terms']").click()
# Working for the button
# driver.find_element_by_xpath("//input[@type='submit']").click()
# Working with the link
driver.find_element_by_link_text("Read Detail").click()

time.sleep(5)
driver.close()
quit()