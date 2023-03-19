from bs4 import BeautifulSoup
import cloudscraper
scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
url = 'https://www.classcentral.com/'
req = scraper.get(url)

# soup = BeautifulSoup(req.content,'lxml')
soup = BeautifulSoup(req.text, "html.parser")
# path, _ = os.path.splitext(pagepath)
# pagefolder = path+'_files' # page contents folder
# tags_inner = {'img': 'src', 'link': 'href', 'script': 'src'} # tag&inner tags to grab
# for tag, inner in tags_inner.items(): # saves resource files and rename refs
#     savenRename(soup, pagefolder, session, url, tag, inner)
# with open(path+'.html', 'wb') as file: # saves modified html doc
#     file.write(soup.prettify('utf-8'))