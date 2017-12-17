#drafter.py
import pandas as pd
import sqlite3
import json

#Alternative to SQL (Uses csv files)
#final_ranks = pd.read_csv('final_rankings.csv')
#avg_ranks = pd.read_csv('avg_draft.csv')
#rankings = pd.read_csv('rankings.csv')

#Converts sqlite database to dataframe

conn = sqlite3.connect('FinalDB.sqlite')
cur = conn.cursor()

projections_df = pd.read_sql_query('SELECT * FROM Scores_VS_Projections;', conn)

final_ranks = pd.read_sql_query('SELECT * FROM Final_Rankings;', conn)
final_ranks['Rank'] = pd.to_numeric(final_ranks['Rank'], errors = 'coerce')

avg_ranks = pd.read_sql_query('SELECT * FROM AVG_Rankings;', conn)
avg_ranks['Rank'] = pd.to_numeric(avg_ranks['Rank'], errors = 'coerce')
class Draft():
	

	def __init__(self):
		self.my_ranks = final_ranks.copy()
		self.my_team = []
		self.my_starters = []
		self.my_backups = []
		self.round = 0
		self.my_wrs = []
		self.my_rbs = []
		self.my_ks = []
		self.my_qbs = []
		self.my_tes = []
		self.my_ds = []

	def pick_player(self, player = ''):
		global final_ranks
		global avg_ranks
		self.my_ranks = final_ranks.copy()
		self.update_ranks()
		player = self.my_ranks['Player'][0]
		print('team selects...', player)
		#print(self.my_ranks['Player'][0])
		#print(self.my_ranks)
		position = self.my_ranks.loc[self.my_ranks['Player'] == player, 'Position'].iloc[0]
		self.my_team.append(player)

		if position == 'wr':
			self.my_wrs.append(player)
			if len(self.my_wrs) <= 3: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'qb':
			self.my_qbs.append(player)
			if len(self.my_qbs) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'rb':
			self.my_rbs.append(player)
			if len(self.my_rbs) <= 2: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'te':
			self.my_tes.append(player)
			if len(self.my_tes) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'k':
			self.my_ks.append(player)
			if len(self.my_ks) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'd':
			self.my_ds.append(player)
			if len(self.my_ds) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		else:
			print('Position Error')
		final_ranks = final_ranks[final_ranks.Player != player]
		final_ranks = final_ranks.reset_index(drop = True)
		if player in avg_ranks['Player'].values:
			avg_ranks = avg_ranks[avg_ranks.Player != player]
			avg_ranks = avg_ranks.reset_index(drop = True)
		pass

	def print_team(self):

		print('WRs:', self.my_wrs)
		print('QBs:', self.my_qbs)
		print('Ds:', self.my_ds)
		print('Ks:', self.my_ks)
		print('TEs:', self.my_tes)
		print('RBs:', self.my_rbs)
		pass

	def update_ranks(self):

		#Update WR ranks
		if(len(self.my_wrs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.2
		if(len(self.my_wrs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.6
		if(len(self.my_wrs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.8
		if(len(self.my_wrs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 2
		if(len(self.my_wrs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 2.2

		#update RB ranks

		if(len(self.my_rbs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.2
		if(len(self.my_rbs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.6
		if(len(self.my_rbs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.8
		if(len(self.my_rbs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 2
		if(len(self.my_rbs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 2.2

		#update qbs
		if(len(self.my_qbs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.2
		if(len(self.my_qbs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.6
		if(len(self.my_qbs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.8
		if(len(self.my_qbs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 2
		if(len(self.my_qbs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 2.2

		#update tes
		if(len(self.my_tes) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.2
		if(len(self.my_tes) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.6
		if(len(self.my_tes) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.8
		if(len(self.my_tes) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 2
		if(len(self.my_tes) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 2.2


		#update d

		if(len(self.my_ds) == 0 and ((len(self.my_tes) + len(self.my_rbs) + len(self.my_wrs) + len(self.my_ks) + len(self.my_qbs)) == 15)):
			self.my_ranks.loc[self.my_ranks.Position == 'd', 'Rank'] = -.1

		if(len(self.my_ds) >= 1):
			self.my_ranks.loc[self.my_ranks.Position == 'd', 'Rank'] *= 3


		#update k
		if(len(self.my_ks) == 0 and ((len(self.my_tes) + len(self.my_rbs) + len(self.my_wrs) + len(self.my_ds) + len(self.my_qbs)) == 14)):
			self.my_ranks.loc[self.my_ranks.Position == 'k', 'Rank'] = 0

		if(len(self.my_ks) >= 1):
			self.my_ranks.loc[self.my_ranks.Position == 'k', 'Rank'] *= 3


		self.my_ranks = self.my_ranks.sort_values(by =['Rank'])
		self.my_ranks = self.my_ranks.reset_index(drop = True)
		#print('updating ranks...')
		pass

class AutoDraft():
	

	def __init__(self):
		self.my_ranks = avg_ranks.copy()
		self.my_team = []
		self.my_starters = []
		self.my_backups = []
		self.round = 0
		self.my_wrs = []
		self.my_rbs = []
		self.my_ks = []
		self.my_qbs = []
		self.my_tes = []
		self.my_ds = []
	def pick_player(self, player = ''):
		global final_ranks
		global avg_ranks
		self.my_ranks = avg_ranks.copy()
		self.update_ranks()
		player = self.my_ranks['Player'][0]
		print('team selects...', player)
		#print(self.my_ranks['Player'][0])
		#print(self.my_ranks)
		position = avg_ranks.loc[avg_ranks['Player'] == player, 'Position'].iloc[0]
		self.my_team.append(player)
		if position == 'wr':
			self.my_wrs.append(player)
			if len(self.my_wrs) <= 3: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'qb':
			self.my_qbs.append(player)
			if len(self.my_qbs) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'rb':
			self.my_rbs.append(player)
			if len(self.my_rbs) <= 2: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'te':
			self.my_tes.append(player)
			if len(self.my_tes) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'k':
			self.my_ks.append(player)
			if len(self.my_ks) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		elif position == 'd':
			self.my_ds.append(player)
			if len(self.my_ds) <= 1: self.my_starters.append(player)
			else: self.my_backups.append(player)
		else:
			print('Position Error')
		if player in final_ranks['Player'].values:
			final_ranks = final_ranks[final_ranks.Player != player]
			final_ranks = final_ranks.reset_index(drop = True)
		avg_ranks = avg_ranks[avg_ranks.Player != player]
		avg_ranks = avg_ranks.reset_index(drop = True)
		pass
	def print_team(self):

		print('WRs:', self.my_wrs)
		print('QBs:', self.my_qbs)
		print('Ds:', self.my_ds)
		print('Ks:', self.my_ks)
		print('TEs:', self.my_tes)
		print('RBs:', self.my_rbs)
		pass

	def update_ranks(self):
		global final_ranks
		#Update WR ranks
		if(len(self.my_wrs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.2
		if(len(self.my_wrs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.6
		if(len(self.my_wrs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.8
		if(len(self.my_wrs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 2
		if(len(self.my_wrs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 2.2

		#update RB ranks

		if(len(self.my_rbs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.2
		if(len(self.my_rbs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.6
		if(len(self.my_rbs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.8
		if(len(self.my_rbs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 2
		if(len(self.my_rbs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 2.2

		#update qbs
		if(len(self.my_qbs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.2
		if(len(self.my_qbs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.6
		if(len(self.my_qbs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.8
		if(len(self.my_qbs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 2
		if(len(self.my_qbs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 2.2

		#update tes
		if(len(self.my_tes) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.2
		if(len(self.my_tes) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.6
		if(len(self.my_tes) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.8
		if(len(self.my_tes) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 2
		if(len(self.my_tes) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 2.2


		#update d

		if(len(self.my_ds) == 0 and ((len(self.my_tes) + len(self.my_rbs) + len(self.my_wrs) + len(self.my_ks) + len(self.my_qbs)) == 15)):
			self.my_ranks.loc[self.my_ranks.Position == 'd', 'Rank'] = -.1

		if(len(self.my_ds) >= 1):
			self.my_ranks.loc[self.my_ranks.Position == 'd', 'Rank'] *= 3


		#update k
		if(len(self.my_ks) == 0 and ((len(self.my_tes) + len(self.my_rbs) + len(self.my_wrs) + len(self.my_ds) + len(self.my_qbs)) == 14)):
			self.my_ranks.loc[self.my_ranks.Position == 'k', 'Rank'] = 0

		if(len(self.my_ks) >= 1):
			self.my_ranks.loc[self.my_ranks.Position == 'k', 'Rank'] *= 3


		self.my_ranks = self.my_ranks.sort_values(by =['Rank'])
		self.my_ranks = self.my_ranks.reset_index(drop = True)
		#print('updating ranks...')
		pass


def main():
	print('Fantasy Mock Draft 2017')
	print('RANKS', final_ranks)
	print('AVG', avg_ranks)

	player1 = Draft()
	player2 = AutoDraft()
	player3 = AutoDraft()
	player4 = AutoDraft()
	player5 = AutoDraft()
	player6 = AutoDraft()
	player7 = AutoDraft()
	player8 = AutoDraft()

	for i in range(16):
		print('Round', i+1)

		print('player 1 picking...')
		player1.pick_player()
		print('player 2 picking...')
		player2.pick_player()
		print('player 3 picking...')
		player3.pick_player()
		print('player 4 picking...')
		player4.pick_player()
		print('player 5 picking...')
		player5.pick_player()
		print('player 6 picking...')
		player6.pick_player()
		print('player 7 picking...')
		player7.pick_player()
		print('player 8 picking...')
		player8.pick_player()


	
		print('Player 1')
		player1.print_team()
		print()

		print('Player 2:')
		player2.print_team()
		print()

		print('Player 3')
		player3.print_team()
		print()

		print('Player 4:')
		player4.print_team()
		print()

		print('Player 5')
		player5.print_team()
		print()

		print('Player 6:')
		player6.print_team()
		print()

		print('Player 7')
		player7.print_team()
		print()

		print('Player 8:')
		player8.print_team()
		print()
		
		# print('FINAL', final_ranks)
		# print('AVG', avg_ranks)

	cur.execute('DROP TABLE IF EXISTS Teams')
	cur.execute('CREATE TABLE Teams (Player1 TEXT, Player2 TEXT, Player3 TEXT, Player4 TEXT, Player5 TEXT, Player6 TEXT, Player7 TEXT, Player8 TEXT)')
	i = 0
	while(i < 16):
		team_tup = player1.my_team[i], player2.my_team[i], player3.my_team[i], player4.my_team[i], player5.my_team[i], player6.my_team[i], player7.my_team[i], player8.my_team[i]
		cur.execute('INSERT INTO Teams VALUES (?, ?, ?, ?, ?, ?, ?, ?)', team_tup)
		conn.commit()
		i += 1
	cur.execute('DROP TABLE IF EXISTS Starters')
	cur.execute('CREATE TABLE Starters (Player1 TEXT, Player2 TEXT, Player3 TEXT, Player4 TEXT, Player5 TEXT, Player6 TEXT, Player7 TEXT, Player8 TEXT)')
	i = 0
	while(i < 9):
		start_tup = player1.my_starters[i], player2.my_starters[i], player3.my_starters[i], player4.my_starters[i], player5.my_starters[i], player6.my_starters[i], player7.my_starters[i], player8.my_starters[i]
		cur.execute('INSERT INTO Starters VALUES (?, ?, ?, ?, ?, ?, ?, ?)', start_tup)
		conn.commit()
		i += 1
	#print(player1.my_ranks['Player'].values)
	def find_score(team, backups, my_ranks):
		team_score = 0
		for player in team:
			if player in projections_df['Player'].values:
				score = projections_df.loc[projections_df['Player'] == player, 'Score'].iloc[0]
				#Accounts for injuries (substitutes highest performing backup)
				if score < 30:
					for backup in backups:
						if backup in projections_df['Player'].values:
							position = projections_df.loc[projections_df['Player'] == player, 'Position'].iloc[0]
							backup_pos = projections_df.loc[projections_df['Player'] == backup, 'Position'].iloc[0]
							if position == backup_pos:
								new_score = projections_df.loc[projections_df['Player'] == backup, 'Score'].iloc[0]
								if new_score > score:
									player = backup
									score = new_score
				#Accounts for lack up backup(Waiver Wire). Assumes first pick on waiver wire
				if score < 30:
					for rank in my_ranks:
						if rank in projections_df['Player'].values:
							position = projections_df.loc[projections_df['Player'] == player, 'Position'].iloc[0]
							waiver_pos = projections_df.loc[projections_df['Player'] == rank, 'Position'].iloc[0]
							if position == waiver_pos:
								waiver_score = projections_df.loc[projections_df['Player'] == rank, 'Score'].iloc[0]
								if waiver_score > score:
									player = rank
									score = waiver_score

				#print(player, score)
			else:
				score = 0
			team_score += score
		return team_score

	cur.execute('DROP TABLE IF EXISTS Team_Score')
	cur.execute('CREATE TABLE Team_Score (Team TEXT, Score NUMBER)')

	#print('Team Results')

	#print('1')
	score_1 = find_score(player1.my_starters, player1.my_backups, player1.my_ranks['Player'].values)
	#print('2')
	score_2 = find_score(player2.my_starters, player2.my_backups, player2.my_ranks['Player'].values)
	#print('3')
	score_3 = find_score(player3.my_starters, player3.my_backups, player3.my_ranks['Player'].values)
	#print('4')
	score_4 = find_score(player4.my_starters, player4.my_backups, player4.my_ranks['Player'].values)
	#print('5')
	score_5 = find_score(player5.my_starters, player5.my_backups, player5.my_ranks['Player'].values)
	#print('6')
	score_6 = find_score(player6.my_starters, player6.my_backups, player6.my_ranks['Player'].values)
	#print('7')
	score_7 = find_score(player7.my_starters, player7.my_backups, player7.my_ranks['Player'].values)
	#print('8')
	score_8 = find_score(player8.my_starters, player8.my_backups, player8.my_ranks['Player'].values)
	#print(player1.my_backups)

	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('1', score_1))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('2', score_2))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('3', score_3))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('4', score_4))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('5', score_5))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('6', score_6))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('7', score_7))
	cur.execute('INSERT INTO Team_Score VALUES (?, ?)', ('8', score_8))

	conn.commit()



if __name__ == '__main__':
	main()