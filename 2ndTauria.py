from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import random
import string
import os


def random_string(length):  
    letters = string.ascii_lowercase # define the specific string  
    # define the condition for random.sample() method  
    result1 = ''.join((random.sample(letters, length)))   
    # print(" Random generated string without repetition: ", result1)
    return result1
ab=random_string(5)
print (ab)

#opening the browser
driver=webdriver.Chrome(executable_path=os.getcwd()+ r"\\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(60)

#setting up workspace
driver.get("https://tauria.com/signin")
driver.find_element_by_xpath("//button[contains(text(),'CREATE ONE')]").click()

# personal details and email
driver.find_element_by_xpath("//input[@id='name']").send_keys(random_string(5))
driver.find_element_by_xpath("/html//div[@id='root']/div/div//form//button[.='NEXT']").click()
driver.find_element_by_xpath("//input[@id='first']").send_keys("Oyes")
driver.find_element_by_xpath("//input[@id='last']").send_keys("Cubes")
driver.find_element_by_xpath("//input[@id='email']").send_keys(random_string(5)+"@mailinator.com")
driver.find_element_by_xpath("/html//div[@id='root']/div/div//form//button[.='NEXT']").click()

#setting password
driver.find_element_by_xpath("//input[@id='password']").send_keys("MojTos2")
driver.find_element_by_xpath("//input[@id='confirm']").send_keys("MojTos2")
driver.find_element_by_xpath("/html//div[@id='root']/div/div//form//button[.='NEXT']").click()

message=driver.find_element_by_xpath("//body/div[@class='o_web_client']/div[@class='ZebuMailOnboarding']//div[@class='OnboardingChoice-title']").text
print(message)




