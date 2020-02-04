from selenium.webdriver import Chrome

path=("/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver")
driver=Chrome(executable_path=path)
driver.maximize_window()
mainWin=""

driver.get("https://www.thetestingworld.com/testings/")
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Delete')]").click()

allTabs=driver.window_handles # Lets displayed all open tabs in the browser in string
print(allTabs)

for tab in allTabs: # Method LOOP lets us to get all open tabs with their URL
    driver.switch_to.window(tab)
    print(driver.current_url)

for tab in allTabs: # Method LOOP lets us to choose necessary tab and perform some task (example: push download button)
    driver.switch_to.window(tab)
    if(driver.current_url=="https://www.thetestingworld.com/testings/manage_customer.php"):
        driver.find_element_by_xpath("//button[text()='Start Download']").click()