from pywebcopy import save_website
save_website(
url="https://www.classcentral.com/",
project_folder="D:\Web Scraping",
project_name="my_site",
bypass_robots=True,
debug=True,
open_in_browser=True,
delay=None,
threaded=False,
)