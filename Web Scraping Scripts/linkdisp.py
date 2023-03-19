import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.classcentral.com/'
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

reqs = requests.get(url,headers=headers)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
count=0
for link in soup.find_all('a'):
    print(link.get('href'))
    count+=1
print(f'count = {count}')