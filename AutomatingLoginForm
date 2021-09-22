from selenium import webdriver
import sys

PATH="D:\chrome driver\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://ahmed0saber.github.io/ehrth/check_valid.html")

user = driver.find_element_by_id("t1")
user.send_keys("ahmed0saber")
password = driver.find_element_by_id("t2")

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                password.send_keys(a,b,c,d)
                print(a,b,c,d)
                driver.find_element_by_tag_name("button").click()
                if(driver.find_element_by_id("p1").text=="Correct Data"):
                    sys.exit()
                password.clear()
