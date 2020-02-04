from selenium.webdriver import Chrome

path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver=Chrome(executable_path=path)

driver.get('https://www.thetestingworld.com/testings/')

driver.execute_script("window.scrollTo(0,400);")