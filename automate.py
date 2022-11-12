import imp
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
print(driver)
driver.maximize_window()
driver.get("https://www.google.co.in")
time.sleep(3)



driver.find_element_by_name("q").send_keys("i phone")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.close()
print("sample test over...")