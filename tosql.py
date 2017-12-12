import sqlite3


conn = sqlite3.connect('FinalDB.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Final_Rankings')
cur.execute('CREATE TABLE Final_Rankings (Index INTEGER, Rank NUMBER, Position TEXT, My Rank NUMBER, AVG Rank NUMBER)')

fr_tup = 
cur.execute('DROP TABLE IF EXISTS AVG_Rankings')
cur.execute('CREATE TABLE Users (user_id TEXT NOT NULL PRIMARY KEY, screen_name TEXT, num_favs INTEGER, description TEXT)')

cur.execute('DROP TABLE IF EXISTS D')

cur.execute('DROP TABLE IF EXISTS K')

cur.execute('DROP TABLE IF EXISTS QB')

cur.execute('DROP TABLE IF EXISTS RB')

cur.execute('DROP TABLE IF EXISTS TE')

cur.execute('DROP TABLE IF EXISTS WR')


def add_table(table):
