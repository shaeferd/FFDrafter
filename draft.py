#draft.py
import pandas as pd

class Draft():
	final_ranks = pd.read_csv('final_rankings.csv')
	avg_ranks = pd.read_csv('avg_draft.csv')
	def __init__(self, my_ranks = final_ranks):
		self.round = 0
		self.my_wrs = []
		self.my_rbs = []
		self.my_ks = []
		self.my_qbs = []
		self.my_tes = []
		self.my_ds = []

	def pick_player(player):

		#enter player and that deletes row from final ranks and avg ranks
		#adds player to list of players
	def print_team():

	def update_ranks():
		#assigns new value to each player and sets my_ranks equal to new ranks
	def team_is_full():
		#returns true if team is full, else returns false
class Autodraft():
	def __init__(self, my_ranks = avg_ranks):

	def pick_player(player):
	def print_team():
	def team_is_full():

	main():
		player1 = draft()
		player2 = draft()
		#while(!team_is_full()):
			
