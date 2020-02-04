from selenium.webdriver import Chrome

path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver=Chrome(executable_path=path)
driver.maximize_window()
driver.get('https://www.trio02.ru/')
size=driver.get_window_size()
print(size)

driver.close()