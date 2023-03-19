from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import os
import codecs
url = 'https://angular.io/' 
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
driver.get(url) 
 
print(driver.page_source)

n = os.path.join("D:\Web Scraping", "classcentral.html")
f = codecs.open(n, "w", "utf−8")
h = driver.page_source
f.write(h)