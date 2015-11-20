import urllib.request
from bs4 import *

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Marla.html"
count = 7
position = 18

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print(url)
