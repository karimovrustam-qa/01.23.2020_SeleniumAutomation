import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select # Required when work with Dropdown or List


path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

driver.maximize_window()

object=Select(driver.find_element_by_name("sex"))
object.select_by_visible_text("Male")

# Fetch selected option
print(object.first_selected_option.text)

# Fetch all available options using LOOP
for option in object.options:
    print(option.text)

driver.close()
quit()