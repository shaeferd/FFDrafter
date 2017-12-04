#avg_draft.py
from bs4 import BeautifulSoup
import urllib.request

def scrape_player_list():
	players = []
	base_url = 'http://subscribers.footballguys.com/apps/adp-ppr.php'
	r = urllib.request.urlopen(base_url)
	r = r.read()
	soup = BeautifulSoup(r, 'lxml')
	for player in soup.find_all('td'):
		for player in player.find_all('a'):
			if(player.text != ''):
				players.append(player.text)

	output = zip(list(range(len(players))),players)
	with open('avg_draft.csv',"w") as outfile:
		outfile.write("Rank,Player\n")
		for player in output:
			outfile.write("{},{}\n".format(*player))


scrape_player_list()