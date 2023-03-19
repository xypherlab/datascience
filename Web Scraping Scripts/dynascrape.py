from selenium import webdriver
import codecs
import os
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.tutorialspoint.com/index.htm")
#get file path to save page
n=os.path.join("D:\Web Scraping","Page.html")
#open file in write mode with encoding
f = codecs.open(n, "w", "utf−8")
#obtain page source
h = driver.page_source
#write page source content to file
f.write(h)
#close browser
driver.quit()