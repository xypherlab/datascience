import urllib.request 
output = open("clone.html", 'w', encoding="utf-8")
def clone(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode()
    return html

user_input = "https://en.wikipedia.org/wiki/Main_Page"
print(clone(user_input), file=output)
#print(clone(user_input), file=output)
print("website cloned successfully, check clone.html :)")