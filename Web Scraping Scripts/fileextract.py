import requests
from bs4 import BeautifulSoup
  
# Web URL
web_url = "https://www.classcentral.com/"
  
# get HTML content
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
html = requests.get(web_url,headers=headers).content
  
# parse HTML Content
soup = BeautifulSoup(html, "html.parser")
  
js_files = []
cs_files = []
  
for script in soup.find_all("script"):
    if script.attrs.get("src"):
        
        # if the tag has the attribute 
        # 'src'
        url = script.attrs.get("src")
        js_files.append(web_url+url)
  
  
for css in soup.find_all("link"):
    if css.attrs.get("href"):
        
        # if the link tag has the 'href'
        # attribute
        _url = css.attrs.get("href")
        cs_files.append(web_url+_url)
  
# adding links to the txt files
with open("javajavascript_files.txt", "w") as f:
    for js_file in js_files:
        print(js_file, file=f)
  
with open("css_files.txt", "w") as f:
    for css_file in cs_files:
        print(css_file, file=f)