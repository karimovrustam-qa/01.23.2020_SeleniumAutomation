from selenium.webdriver import Chrome


path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

driver.maximize_window()

# Get title from WEB-page
print("Title of the page is: " + driver.title)

# Get URL of the page
print("URL of the page is: " + driver.current_url)

# Fetch complete page HTML
print("*****************************************************")
print(driver.page_source)

# Fetching element text
print("Text on Link is: " + driver.find_element_by_class_name("displayPopup").text)

# Fetching attribute value of element
print("Value of Button is: " + driver.find_element_by_xpath("//input[@type='submit']").get_attribute('value'))