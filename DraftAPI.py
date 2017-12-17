#DraftAPI.py
import requests
import json
import csv
from pprint import pprint
import sqlite3
import urllib.request


CACHE_FNAME = "ADP.json"


try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}


def get_rankings(api):
	global CACHE_DICTION
	if api in CACHE_DICTION:
		print('using cache...')
	else:
		print('fetching...')
		if(api == 'NFL'):
			CACHE_DICTION[api] = []
			offset = 0
			count = 50
			while(offset < 300):
				url_params = {}
				url_params['offset'] = offset
				url_params['season'] = 2017
				url_params['count'] = 50
				url_params['format'] = 'json'
				baseurl = 'http://api.fantasy.nfl.com/v1/players/editordraftranks'
				req = requests.get(baseurl, params = url_params)
				clean_data = json.loads(req.text)
				CACHE_DICTION[api].append(clean_data['players'])
				dumped_json_cache = json.dumps(CACHE_DICTION, indent = 4)
				fw = open(CACHE_FNAME,"w")
				fw.write(dumped_json_cache)
				offset += 50
				count += 50
				fw.close()

get_rankings('NFL')


CACHE_FNAME = "season_pts.json"


# Put the rest of your caching setup here:
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION_2 = json.loads(cache_contents)
except:
    CACHE_DICTION_2 = {}
def get_pts(api):
	if api in CACHE_DICTION_2:
		print('using cache...')
	else:
		print('fetching...')
		CACHE_DICTION_2[api] = {}
		week = 14
		url_params = {}
		url_params['statType'] = 'seasonStats'
		url_params['season'] = 2017
		url_params['week'] = week
		url_params['format'] = 'json'
		baseurl = 'http://api.fantasy.nfl.com/v1/players/stats'
		req = requests.get(baseurl, params = url_params)
		clean_data = json.loads(req.text)
		CACHE_DICTION_2[api]['szn_pts'] = clean_data['players']
		dumped_json_cache = json.dumps(CACHE_DICTION_2, indent = 4)
		fw = open(CACHE_FNAME,"w")
		fw.write(dumped_json_cache)
		fw.close()
	return CACHE_DICTION_2[api]['szn_pts']

get_pts('NFL')

conn = sqlite3.connect('FinalDB.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Scores_VS_Projections')
cur.execute('CREATE TABLE Scores_VS_Projections (Player TEXT, Position TEXT, Projected NUMBER, Score NUMBER)')
def projected_to_actual():
	player = []
	projected = []
	actual = []
	szn_stats = get_pts('NFL')
	for stat in szn_stats:
		tup = stat['name'], stat['position'], stat['seasonProjectedPts'], stat['seasonPts']
		cur.execute('INSERT INTO Scores_VS_Projections VALUES (?, ?, ?, ?)', tup)
		conn.commit()

projected_to_actual()
