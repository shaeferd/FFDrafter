#projections.py
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('FinalDB.sqlite')
cur = conn.cursor()
projections_df = pd.read_sql_query('SELECT * FROM Scores_VS_Projections;', conn)

projected = [num for lst in cur.execute('SELECT Projected FROM Scores_VS_Projections').fetchall() for num in lst]
score = [num for lst in cur.execute('SELECT Score FROM Scores_VS_Projections').fetchall() for num in lst]

projections_df.plot('Projected', 'Score', kind = 'scatter', title = 'Scores Vs Projections')

plt.show()



