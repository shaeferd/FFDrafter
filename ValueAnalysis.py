import pandas as pd
import sqlite3
# QB_df = pd.read_csv('qb.csv')
# RB_df = pd.read_csv('rb.csv')
# TE_df = pd.read_csv('te.csv')
# D_df = pd.read_csv('d.csv')
# K_df = pd.read_csv('K.csv')
# WR_df = pd.read_csv('wr.csv')
# avg_draft = pd.read_csv('avg_draft.csv')
conn = sqlite3.connect('FinalDB.sqlite')

QB_df = pd.read_sql_query('SELECT * FROM QB;', conn)
RB_df = pd.read_sql_query('SELECT * FROM RB;', conn)
TE_df = pd.read_sql_query('SELECT * FROM TE;', conn)
D_df = pd.read_sql_query('SELECT * FROM D;', conn)
K_df = pd.read_sql_query('SELECT * FROM K;', conn)
WR_df = pd.read_sql_query('SELECT * FROM WR;', conn)
avg_draft = pd.read_sql_query('SELECT * FROM AVG_Rankings;', conn)

#add ranks to avg draft (will be used later)
if 'Rank' not in avg_draft: avg_draft.insert(0, 'Rank', avg_draft.index)

#add position
if 'Position' not in QB_df: QB_df.insert(2, 'Position', ['qb']*len(QB_df['Player']))
if 'Position' not in RB_df: RB_df.insert(2, 'Position', ['rb']*len(RB_df['Player']))
if 'Position' not in TE_df: TE_df.insert(2, 'Position', ['te']*len(TE_df['Player']))
if 'Position' not in D_df: D_df.insert(2, 'Position', ['d']*len(D_df['Player']))
if 'Position' not in K_df: K_df.insert(2, 'Position', ['k']*len(K_df['Player']))
if 'Position' not in WR_df: WR_df.insert(2, 'Position', ['wr']*len(WR_df['Player']))

# def cache_csv(file_name):
# 	try:
# 		pd.read_csv(file_name+'.csv')
# 		print('reading from cache')
# 	except:
		
def value_score(my_file):
	#Average number of players drafted per position for the first 100 picks
	if 'Player' in my_file.keys():
		if my_file['Player'][0] == QB_df['Player'][0]: num_players = 15
		elif my_file['Player'][0] == RB_df['Player'][0]: num_players = 36
		elif my_file['Player'][0] == TE_df['Player'][0]: num_players = 8
		elif my_file['Player'][0] == WR_df['Player'][0]: num_players = 38
		elif my_file['Player'][0] == D_df['Player'][0]: num_players = 2
		elif my_file['Player'][0] == K_df['Player'][0]: num_players = 1
	else: print('unknown file name')

	baseline_score = my_file['PTS'][:num_players].min()
	my_file['Score'] = my_file['PTS'] - baseline_score

	return my_file['Score']
	
def get_rankings():
	value_score(QB_df), value_score(RB_df), value_score(TE_df), value_score(WR_df), value_score(D_df), value_score(K_df)
	df = QB_df.copy()
	df = df.append([RB_df, TE_df, WR_df, D_df, K_df])
	df = df.sort_values('Score', ascending = False)
	df = df.reset_index(drop = True)
	df = df[['Player','Position','Score']]
	ind = list(df.index.values)
	#print(ind)
	if 'Rank' not in df: df.insert(0, 'Rank', ind)
	try:
		print('reading from cache')
		#pd.read_csv('rankings.csv')
		pd.read_sql_query('SELECT * FROM Rankings;', conn)
	except:
		print('creating new rankings list')
		#df.to_csv('rankings.csv')
		df.to_sql('Rankings', conn, if_exists='replace')
	df = df[:286]
	return df

def get_avg_rankings():
	return avg_draft

def find_rank(player, rankings = get_rankings()):
	return int(rankings.loc[rankings['Player'] == player, 'Rank'].iloc[0])

def find_avg_rank(player):
	return int(avg_draft.loc[avg_draft['Player'] == player, 'Rank'].iloc[0])

def find_position(player, rankings = get_rankings()):
	return rankings.loc[rankings['Player'] == player, 'Position'].iloc[0]

def final_rankings(avg_rankings = get_avg_rankings(), rankings = get_rankings()):
	final_rankings = pd.DataFrame(columns = ['Rank', 'Player', 'Position', 'My Rank', 'Avg Rank'], index = list(range(len(avg_rankings))))
	count = 0
	for player in rankings['Player']:
		#print(player)
		#print(avg_rankings['Player'].values)
		if player in avg_rankings['Player'].values:
			rank = find_rank(player)
			avg_rank = find_avg_rank(player)
			position = find_position(player)
			if avg_rank > rank:
				new_rank = (avg_rank + rank) / 2
			else:
				new_rank = rank
			final_rankings.ix[count] = [new_rank, player, position, rank, avg_rank]
			count += 1
		else:
			continue
	final_rankings = final_rankings.sort_values(by =['Rank'])
	final_rankings = final_rankings.dropna(how ='all')
	final_rankings = final_rankings.reset_index(drop = True)
	final_rankings.to_csv('final_rankings.csv')
	final_rankings.to_sql('Final_Rankings', conn, if_exists='replace')
	return final_rankings

def main():

	#print(get_rankings())
	#print(avg_draft)
	final = final_rankings()
	print(final)
	#print(find_position('Broncos'))
	#print(get_rankings())
	#print(find_position('David Johnson'))

if __name__ == '__main__':
	main()