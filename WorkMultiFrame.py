from selenium.webdriver import Chrome

path=("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
driver=Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.toolsqa.com/iframe-practice-page/")


# driver.switch_to.frame("iframe2") # When working with few windows, you need switch to necessary
# # or
# # driver.switch_to.frame("IF2")
# # or
# # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='iframe2']"))
# driver.find_element_by_xpath("//a[contains(text(),'Read more')]").click()

driver.switch_to.default_content() # When you need stop working with one window, and come to whole page
driver.find_element_by_xpath("//span[text()='VIDEOS']").click()

# TODO: Could not reproduce looking for XPath through switching windows. Repeat it!