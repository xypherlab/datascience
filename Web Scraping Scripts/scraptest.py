from bs4 import BeautifulSoup

html = """<div>something</div>
<div>something else</div>
<div class='magical'>hi there</div>
<p>ok</p>
"""

soup = BeautifulSoup(html, "html.parser")

print([str(tag) for tag in soup.find_all()])