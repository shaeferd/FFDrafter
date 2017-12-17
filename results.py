#results.py
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('FinalDB.sqlite')
cur = conn.cursor()
team_score_df = pd.read_sql_query('SELECT * FROM Team_Score;', conn)

team = [num for lst in cur.execute('SELECT Team FROM Team_Score').fetchall() for num in lst]
score = [num for lst in cur.execute('SELECT Score FROM Team_Score').fetchall() for num in lst]


team_score_df.plot('Team', 'Score', kind = 'bar', title = 'Estimated Score Per Team')
plt.show()
