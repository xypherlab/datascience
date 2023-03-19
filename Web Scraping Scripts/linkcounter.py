from requests_html import HTMLSession
from collections import Counter
from urllib.parse import urlparse

session = HTMLSession()
r = session.get("https://www.classcentral.com/")
unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
for link in unique_netlocs:
    print(link, unique_netlocs[link])

