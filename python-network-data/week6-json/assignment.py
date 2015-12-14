import json
import urllib.request

address = "http://python-data.dr-chuck.net/comments_167252.json"
response = urllib.request.urlopen(address).read().decode('utf-8')
data = json.loads(response)

sum = 0
for entry in data['comments']:
    sum += entry['count']

print(sum)
