from selenium import webdriver
import keyboard

PATH="D:\chrome driver\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://mathexams.herokuapp.com/")

while keyboard.is_pressed('q') == False:
    num1=int(driver.find_element_by_id("num1").text)
    num2=int(driver.find_element_by_id("num2").text)
    op=driver.find_element_by_id("op").text
    if(op=="+"):
        print(num1+num2)
    elif(op=="-"):
        print(num1-num2)
    elif(op=="*"):
        print(num1*num2)
    elif(op=="/"):
        print(int(num1/num2))
