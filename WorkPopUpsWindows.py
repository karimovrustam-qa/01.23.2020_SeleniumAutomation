from selenium.webdriver import Chrome

path="/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver=Chrome(executable_path=path)
driver.maximize_window()
mainWin=""
driver.get('https://www.naukri.com')
allwindows=driver.window_handles # Get data on all pop-ups by URL in string
# print(allwindows)

# for win in allwindows: # Get data on all pop-ups with URL using LOOP
#     driver.switch_to.window(win)
#     print(driver.current_url)

# for win in allwindows: # This method LOOP lets to close ALL pop-ups windows, except indicated URL, if you don't need current URL
#     driver.switch_to.window(win)
#     print(driver.current_url)
#     if(driver.current_url=="https://www.naukri.com/"):
#         print("This is my main window")
#     else:
#         driver.close()

for win in allwindows: # Same method, like upper, but lets us displayed current URL window, after were closed pop-ups windows
    driver.switch_to.window(win)
    print(driver.current_url)
    if(driver.current_url=="https://www.naukri.com/"):
        mainWin=win
    else:
        driver.close()
driver.switch_to.window(mainWin)
print(driver.current_url) # Get current open window URL