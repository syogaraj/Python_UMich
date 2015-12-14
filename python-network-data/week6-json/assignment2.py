import urllib.parse
import urllib.request
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = "Florida Atlantic University"

url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
data = urllib.request.urlopen(url).read().decode('utf-8')

try: js = json.loads(data)
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')

# print(json.dumps(js, indent=4))

for entry in js['results']:
    print(entry['place_id'])
