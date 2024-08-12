import sys
import json
import requests
from prettytable import PrettyTable

tags = []
args = sys.argv[1:]

for arg in args:
  res = requests.get('https://medium.com/_/api/tags?source=typeahead&q=' + arg)
  payload = res.text.replace('])}while(1);</x>', '')
  count = json.loads(payload)['payload']['value'][0]['postCount']

  tags.append({ 'tag': arg, 'count': count })

results = sorted(tags, reverse=True, key=lambda dict: dict['count'])

table = PrettyTable(['Tag', 'Count'])
for result in results:
  table.add_row([result['tag'], result['count']])

print(table)