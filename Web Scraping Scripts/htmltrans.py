from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
from googletrans import Translator
import requests

translator = Translator()

class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v

files_from_folder = r"D:\Web Scraping\Translated"

use_translate_folder = False

destination_language = 'hi'

extension_file = ".html"

import os

directory = os.fsencode(files_from_folder)
retry=10
def recursively_translate(node):
    for x in range(len(node.contents)):
        if isinstance(node.contents[x], str):
            for i in range(retry):
                if node.contents[x].strip() != '':
                    try:
                        node.contents[x].replaceWith(translator.translate(node.contents[x], dest=destination_language).text)
                        print(node.contents[x])
                        break
                    except Exception as e:
                        print('--------------------------------------------------------------------------------------------------------------------------------------------')
                        print(f'Error: {e}')
                        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        elif node.contents[x] != None:
            recursively_translate(node.contents[x])
        
# for file in os.listdir(directory):
progress=0
total = 0
for root_dir, cur_dir, files in os.walk(directory):
    for f in files:
        if f.endswith(extension_file):
            total += len(files)
print('file total:', total)

for (root, dirs, file) in os.walk(directory):
  
  for f in file:
    progress+=1 
    filename = os.fsdecode(f)
    print(filename)
    dirfile=root.decode()
    print(dirfile)
    if filename.endswith(extension_file):
        with open(os.path.join(dirfile, filename), encoding='utf-8') as html:
            #tags = ['style', 'path','svg', 'meta', '[document]','script']
            # tags=[]
            soup = BeautifulSoup('<pre>' + html.read() + '</pre>', 'html.parser')
            # for t in tags:
            #      [s.extract() for s in soup(t)]
            for title in soup.findAll('title'):
                recursively_translate(title)

            for meta in soup.findAll('meta', {'name':'description'}):
                try:
                    meta['content'] = translator.translate(meta['content'], dest=destination_language).text
                except:
                    pass
   
            count=0
            for tag in soup.find_all():
                if str(tag.string)=='None':
                    pass
                else:
                    print(f'{dirfile}/{filename}<{tag.name}> count({count}) - {round(float(progress/total)*100,2)}% or {progress} out of {total}= {str(tag.get_text())}')

                    recursively_translate(tag)
                count+=1
            

        print(f'{filename} translated')
        soup = soup.encode(formatter=UnsortedAttributes()).decode('utf-8')
        new_filename = f'{filename.split(".")[0]}.html'
        with open(os.path.join(dirfile, new_filename), 'w', encoding='utf-8') as new_html:
                    new_html.write(soup[5:-6])
        if use_translate_folder:
            try:
                with open(os.path.join(dfiles_from_folder+r'\translated', new_filename), 'w', encoding='utf-8') as new_html:
                    new_html.write(soup[5:-6])
            except:
                os.mkdir(files_from_folder+r'\translated')
                with open(os.path.join(dirfile+r'\translated', new_filename), 'w', encoding='utf-8') as new_html:
                    new_html.write(soup[5:-6])
        else:
            with open(os.path.join(dirfile, new_filename), 'w', encoding='utf-8') as html:
                html.write(soup[5:-6])