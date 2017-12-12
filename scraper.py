#from espnff import League


import requests
import json
import csv
from pprint import pprint

# baseurl = 'http://api.fantasy.nfl.com/v1/players/editordraftranks'
# url_params = {}
# url_params['count'] = 100
# url_params['format'] = 'json'
# #'http://api.fantasy.nfl.com/v1/players/stats?statType=seasonStats&season=2010&week=1&format=json'
# req = requests.get(baseurl, params = url_params)
# clean_data = json.loads(req.text)
# pprint(clean_data)

csvfile = open('final_rankings.csv', 'r')
jsonfile = open('cache.json', 'w')

fieldnames = ('Index','Rank','Player','Position','My Rank','Avg Rank')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['final_rankings'] = [row for row in reader]
out = json.dumps( [ row for row in reader ], indent = 4)
jsonfile.write(out)