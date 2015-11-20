import urllib.request
import xml.etree.ElementTree as ET

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_167248.xml"
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')

sum = 0

for count in counts:
    sum += int(count.text)

print(sum)
