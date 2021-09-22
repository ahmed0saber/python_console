from selenium import webdriver
import time

PATH="D:\chrome driver\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://google.com")

search=driver.find_element_by_name("q")
search.send_keys("Naruto")

time.sleep(5)

button=driver.find_element_by_name("btnK")
button.click()
