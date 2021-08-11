from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import os




def factorial_func(num):
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial

driver=webdriver.Chrome(executable_path=os.getcwd()+ r"\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost:6464/")
num_to_calc = 7
driver.find_element_by_xpath("//input[@id='number']").send_keys(num_to_calc)
driver.find_element_by_xpath("//button[@id='getFactorial']").click()
time.sleep(3)

result = driver.find_element_by_xpath("//p[@id='resultDiv']").text
#Gettingthe index of amount int the string and cutting it off
index = result.find(": ") + 2
ui_amount = result[index:]
# converting the amount string to integer
ui_amount = int(ui_amount)
#calculating the factorial
actual_factorail = factorial_func(num_to_calc)

#asserting that what was input on the UI returns correct result
assert ui_amount == actual_factorail
print("Amounts are equal.\nTest passed.") 
 
