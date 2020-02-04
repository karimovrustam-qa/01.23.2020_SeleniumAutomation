from selenium.webdriver import Chrome
import logging # Import LIB

# Step 1
path = "/Users/karimovrustam/PycharmProjects/01.23.2020_SeleniumAutomation/drivers/chromedriver"
driver = Chrome(executable_path=path)
# driver.maximize_window()
# driver.get("https://www.thetestingworld.com/testings")

# Step 2
log=logging.getLogger(__name__) # Create name
log.setLevel(logging.DEBUG) # Create level

# Step 3
warning=logging.FileHandler('./GenerateLOGS/Warning_logs.txt')
warning.setLevel(logging.WARNING)

info=logging.FileHandler('./GenerateLOGS/Info_logs.txt')
info.setLevel(logging.INFO)

# Step 4
formatter=logging.Formatter('%(asctime)s - %(name)s - %levelname)s - %(message)s')

# Step 5
warning.setFormatter(formatter)
info.setFormatter(formatter)

driver.maximize_window()
driver.get("https://www.thetestingworld.com/testings")
log.info("[My URL is Opened]")
log.warning("[There is delay in opening of browser]")