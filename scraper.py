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
CACHE_DICTION = {}
CACHE_DICTION['final_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('avg_draft.csv', 'r')

fieldnames = ('Rank','Player')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['avg_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('d.csv', 'r')

fieldnames = ('Player','TT','SCK','FF','FR','INT','ITD','FTD','PTS')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['d_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('k.csv', 'r')

fieldnames = ('Player','R1','R2','R3','TOT','XP','PTS')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['k_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('qb.csv', 'r')
fieldnames = ('Rank','Player','Position','CA','Pass_YDS','Pass_TD','INT','RUSH','Rush_YDS','Pass_TD','REC','Rec_YDS','Rec_TD','PTS')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['qb_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('rb.csv', 'r')
fieldnames = ('Player','CA','Pass_YDS','Pass_TD','INT','RUSH','Rush_YDS','Pass_TD','REC','Rec_YDS','Rec_TD','PTS')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['rb_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('te.csv', 'r')
fieldnames = ('Player','CA','Pass_YDS','Pass_TD','INT','RUSH','Rush_YDS','Pass_TD','REC','Rec_YDS','Rec_TD','PTS')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['te_rankings'] = [row for row in reader]
csvfile.close()

csvfile = open('wr.csv', 'r')
fieldnames = ('Player','CA','Pass_YDS','Pass_TD','INT','RUSH','Rush_YDS','Pass_TD','REC','Rec_YDS','Rec_TD','PTS')
reader = csv.DictReader(csvfile, fieldnames)
CACHE_DICTION['wr_rankings'] = [row for row in reader]
csvfile.close()

out = json.dumps(CACHE_DICTION, indent = 4)
jsonfile.write(out)


