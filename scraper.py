#from espnff import League


import requests
import json
import csv
from pprint import pprint
import sqlite3
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





conn = sqlite3.connect('FinalDB.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Final_Rankings')
cur.execute('CREATE TABLE Final_Rankings (Count NUMBER, Rank NUMBER, Player TEXT, Position TEXT, My_Rank NUMBER, AVG_Rank NUMBER)')
#final_ranks
for player in CACHE_DICTION['final_rankings'][1:]:
	fr_tup = player['Index'], player['Rank'], player['Player'], player['Position'], player['My Rank'], player['Avg Rank']
	cur.execute('INSERT INTO Final_Rankings VALUES (?, ?, ?, ?, ?, ?)', fr_tup)
	conn.commit()

#avg_ranks
cur.execute('DROP TABLE IF EXISTS AVG_Rankings')
cur.execute('CREATE TABLE AVG_Rankings (Rank NUMBER, Player TEXT)')


for player in CACHE_DICTION['avg_rankings']:
	ar_tup = player['Rank'], player['Player']
	cur.execute('INSERT INTO AVG_Rankings VALUES (?, ?)', ar_tup)
	conn.commit()

#d
cur.execute('DROP TABLE IF EXISTS D')
cur.execute('CREATE TABLE D (Player TEXT,TT NUMBER,SCK NUMBER,FF NUMBER,FR NUMBER ,INT NUMBER,ITD NUMBER,FTD NUMBER,PTS NUMBER)')

for player in CACHE_DICTION['d_rankings'][1:]:
	dr_tup = player['Player'], player['TT'], player['SCK'], player['FF'], player['FR'], player['INT'], player['ITD'], player['FTD'], player['PTS']
	cur.execute('INSERT INTO D VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', dr_tup)
	conn.commit()

#k
cur.execute('DROP TABLE IF EXISTS K')
cur.execute('CREATE TABLE K (Player TEXT,R1 NUMBER,R2 NUMBER,R3 NUMBER,TOT NUMBER ,XP NUMBER,PTS NUMBER)')

for player in CACHE_DICTION['k_rankings'][1:]:
	kr_tup = player['Player'], player['R1'], player['R2'], player['R3'], player['TOT'], player['XP'], player['PTS']
	cur.execute('INSERT INTO K VALUES (?, ?, ?, ?, ?, ?, ?)', kr_tup)
	conn.commit()

#qb
cur.execute('DROP TABLE IF EXISTS QB')
cur.execute('CREATE TABLE QB (Rank NUMBER, Player TEXT,Position TEXT, CA NUMBER, Pass_YDS NUMBER, Pass_TD NUMBER, INT NUMBER, RUSH NUMBER, Rush_YDS NUMBER, REC NUMBER, Rec_YDS NUMBER, Rec_TD NUMBER, PTS NUMBER)')

for player in CACHE_DICTION['qb_rankings'][1:]:
	qr_tup = player['Rank'], player['Player'], player['Position'], player['CA'], player['Pass_YDS'], player['Pass_TD'], player['INT'], player['RUSH'], player['Rush_YDS'], player['REC'], player['Rec_YDS'], player['Rec_TD'], player['PTS']
	cur.execute('INSERT INTO QB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', qr_tup)
	conn.commit()

#rb
cur.execute('DROP TABLE IF EXISTS RB')
cur.execute('CREATE TABLE RB (Player TEXT, CA NUMBER, Pass_YDS NUMBER, Pass_TD NUMBER, INT NUMBER, RUSH NUMBER, Rush_YDS NUMBER, REC NUMBER, Rec_YDS NUMBER, Rec_TD NUMBER, PTS NUMBER)')

for player in CACHE_DICTION['rb_rankings'][1:]:
	rr_tup = player['Player'], player['CA'], player['Pass_YDS'], player['Pass_TD'], player['INT'], player['RUSH'], player['Rush_YDS'], player['REC'], player['Rec_YDS'], player['Rec_TD'], player['PTS']
	cur.execute('INSERT INTO RB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', rr_tup)
	conn.commit()

#wr
cur.execute('DROP TABLE IF EXISTS WR')
cur.execute('CREATE TABLE WR (Player TEXT, CA NUMBER, Pass_YDS NUMBER, Pass_TD NUMBER, INT NUMBER, RUSH NUMBER, Rush_YDS NUMBER, REC NUMBER, Rec_YDS NUMBER, Rec_TD NUMBER, PTS NUMBER)')

for player in CACHE_DICTION['wr_rankings'][1:]:
	wr_tup = player['Player'], player['CA'], player['Pass_YDS'], player['Pass_TD'], player['INT'], player['RUSH'], player['Rush_YDS'], player['REC'], player['Rec_YDS'], player['Rec_TD'], player['PTS']
	cur.execute('INSERT INTO WR VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', wr_tup)
	conn.commit()
#te

cur.execute('DROP TABLE IF EXISTS TE')
cur.execute('CREATE TABLE TE (Player TEXT, CA NUMBER, Pass_YDS NUMBER, Pass_TD NUMBER, INT NUMBER, RUSH NUMBER, Rush_YDS NUMBER, REC NUMBER, Rec_YDS NUMBER, Rec_TD NUMBER, PTS NUMBER)')

for player in CACHE_DICTION['te_rankings'][1:]:
	tr_tup = player['Player'], player['CA'], player['Pass_YDS'], player['Pass_TD'], player['INT'], player['RUSH'], player['Rush_YDS'], player['REC'], player['Rec_YDS'], player['Rec_TD'], player['PTS']
	cur.execute('INSERT INTO TE VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tr_tup)
	conn.commit()












