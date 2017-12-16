#drafter.py
import pandas as pd
final_ranks = pd.read_csv('final_rankings.csv')
avg_ranks = pd.read_csv('avg_draft.csv')
rankings = pd.read_csv('rankings.csv')
class Draft():
	

	def __init__(self):
		self.my_ranks = final_ranks.copy()#[:]
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
		self.my_ranks = final_ranks.copy()#[:]
		self.update_ranks()
		player = self.my_ranks['Player'][0]
		print('team selects...', player)
		print(self.my_ranks['Player'][0])
		print('next', self.my_ranks['Player'][1])
		print(self.my_ranks)
		position = self.my_ranks.loc[self.my_ranks['Player'] == player, 'Position'].iloc[0]
		if position == 'wr':
			self.my_wrs.append(player)
		elif position == 'qb':
			self.my_qbs.append(player)
		elif position == 'rb':
			self.my_rbs.append(player)
		elif position == 'te':
			self.my_tes.append(player)
		elif position == 'k':
			self.my_ks.append(player)
		elif position == 'd':
			self.my_ds.append(player)
		else:
			print('Position Error')
		final_ranks = final_ranks[final_ranks.Player != player]
		#self.update_ranks() #build this class to update according to positions on roster
		final_ranks = final_ranks.reset_index(drop = True)
		avg_ranks = avg_ranks[avg_ranks.Player != player]
		#self.update_ranks()
		avg_ranks = final_ranks.reset_index(drop = True)
		pass
		#enter player and that deletes row from final ranks and avg ranks
		#adds player to list of players
	def print_team(self):

		print('WRs:', self.my_wrs)
		print('QBs:', self.my_qbs)
		print('Ds:', self.my_ds)
		print('Ks:', self.my_ks)
		print('TEs:', self.my_tes)
		print('RBs:', self.my_rbs)
		pass

	#TODO: ADD KICKERS AND DEFENSE AND OTHER POSITIONS
	def update_ranks(self):

		#Update WR ranks
		if(len(self.my_wrs) == 3):
			print('true')
			print(self.my_wrs)
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.2
		elif(len(self.my_wrs) == 4):
			print(self.my_wrs)
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.6
		elif(len(self.my_wrs) == 5):
			print(self.my_wrs)
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.8
		elif(len(self.my_wrs) == 6):
			print(self.my_wrs)
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 2
		elif(len(self.my_wrs) > 6):
			print(self.my_wrs)
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 2.2

		#update RB ranks

		if(len(self.my_rbs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.2
		elif(len(self.my_rbs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.6
		elif(len(self.my_rbs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 1.8
		elif(len(self.my_rbs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 2
		elif(len(self.my_rbs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'rb', 'Rank'] *= 2.2

		#update qbs
		if(len(self.my_qbs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.2
		elif(len(self.my_qbs) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.6
		elif(len(self.my_qbs) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 1.8
		elif(len(self.my_qbs) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 2
		elif(len(self.my_qbs) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'qb', 'Rank'] *= 2.2

		#update tes
		if(len(self.my_tes) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.2
		elif(len(self.my_tes) == 4):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.6
		elif(len(self.my_tes) == 5):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 1.8
		elif(len(self.my_tes) == 6):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 2
		elif(len(self.my_tes) > 6):
			self.my_ranks.loc[self.my_ranks.Position == 'te', 'Rank'] *= 2.2





		self.my_ranks = self.my_ranks.sort_values(by =['Rank'])
		self.my_ranks = self.my_ranks.reset_index(drop = True)
		print('updating ranks...')
		pass
		#assigns new value to each player and sets my_ranks equal to new ranks
	# def team_is_full():
	# 	pass
		#returns true if team is full, else returns false

#copy the final draft rankings to each class instance. Also change rankings based on changes other class instances make
#aka: copy new class instance every time it is called

"""
class AutoDraft():

	def __init__(self, ranks):
		self.my_ranks = ranks[:]
		self.round = 0
		self.my_wrs = []
		self.my_rbs = []
		self.my_ks = []
		self.my_qbs = []
		self.my_tes = []
		self.my_ds = []

	def pick_player(self, player = self.my_ranks['Player'][0]):
		#self.my_ranks
		#global avg_ranks
		position = final_ranks.loc[final_ranks['Player'] == player, 'Position'].iloc[0]
		if position == 'wr':
			self.my_wrs.append(player)
		elif position == 'qb':
			self.my_qbs.append(player)
		elif position == 'rb':
			self.my_rbs.append(player)
		elif position == 'te':
			self.my_tes.append(player)
		elif position == 'k':
			self.my_ks.append(player)
		elif position == 'd':
			self.my_ds.append(player)
		else:
			print('Position Error')
		final_ranks = final_ranks[self.my_ranks.Player != player]
		self.update_ranks()
		final_ranks = final_ranks.reset_index(drop = True)
		avg_ranks = avg_ranks[avg_ranks.Player != player]
		self.update_ranks()
		avg_ranks = avg_ranks.reset_index(drop = True)
		pass
		#enter player and that deletes row from final ranks and avg ranks
		#adds player to list of players
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
		#global avg_ranks
		#if the position certain amount of players, update ranks for position

		#df.loc[df.ID == 103, 'FirstName'] = "Matt"
		self.my_ranks = final_ranks[:]
		if(len(self.my_wrs) == 3):
			self.my_ranks.loc[self.my_ranks.Position == 'wr', 'Rank'] *= 1.2
			#avg_ranks.loc[avg_ranks.Position == 'wr', 'Rank'] *= 1.2

		self.my_ranks = self.my_ranks.sort_values(by =['Rank'])
		pass
		#assigns new value to each player and sets my_ranks equal to new ranks
	def team_is_full():
		pass
		#returns true if team is full, else returns false

"""

def main():
	print('Fantasy Mock Draft 2017')

	print('RANKS', final_ranks)
	player1 = Draft()
	player2 = Draft()
	player3 = Draft()
	player4 = Draft()
	player5 = Draft()
	player6 = Draft()
	player7 = Draft()
	player8 = Draft()

	for i in range(16):
		print('Round', i+1)
		#come up w a way to re-enter
		# player1.pick_player(input('Your Pick:'))
		# player1.pick_player(final_ranks['Player'][0])
		# player2.pick_player(avg_ranks['Player'][0])
		# player3.pick_player(avg_ranks['Player'][0])
		# player4.pick_player(avg_ranks['Player'][0])
		# player5.pick_player(avg_ranks['Player'][0])
		# player6.pick_player(avg_ranks['Player'][0])
		# player7.pick_player(avg_ranks['Player'][0])
		# player8.pick_player(avg_ranks['Player'][0])

		#player1.pick_player(input('Your Pick:'))
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
		
		print('FINAL', final_ranks)
		print('AVG', avg_ranks)

	player2 = Draft()
if __name__ == '__main__':
	main()