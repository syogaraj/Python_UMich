import urllib.request
from bs4 import BeautifulSoup

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_167251.html"
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum = 0
for tag in tags:
    sum += int(tag.contents[0])
    # print('Contents:', tag.contents[0])

print(sum)