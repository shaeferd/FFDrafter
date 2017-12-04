#espn_script.py
from bs4 import BeautifulSoup
import urllib.request

QB = '0'
RB = '2'
WR = '4'
TE = '6'
D = '16'
K = '17'

def scrape_position_data(position_name, position, year, player_list = [], CA_list = [], Pass_YDS_list = [], Pass_TD_list = [], INT_list = [], RUSH_list = [], Rush_YDS_list = [], Rush_TD_list = [], REC_list = [], Rec_YDS_list = [], Rec_TD_list = [], PTS_list = []):	
	start_index = 0
	base_url = 'http://games.espn.com/ffl/tools/projections?&seasonTotals=true&seasonId='+str(year)+'&slotCategoryId='+position
	r = urllib.request.urlopen(base_url)
	r = r.read()
	soup = BeautifulSoup(r, 'lxml')
	if(position_name == 'qb'):
		end_count = 161
	elif(position_name == 'rb'):
		end_count = 149
	elif(position_name == 'te'):
		end_count = 153
	else:
		end_count = 150
	print(base_url)
	while(start_index <= 40):
		for player in soup.find_all('tr'):
			for player_name in player.find_all('a')[93:end_count]:
				if(player_name.text != '' and player_name.text != 'PTS'):
					player_list.append(player_name.text)
			count = 0
			for stats in player.find_all(class_ = 'playertableStat')[11:]:
				if(count == 11): count = 0
				if(count == 0): CA_list.append(stats.text)
				elif(count == 1): Pass_YDS_list.append(stats.text)
				elif(count == 2): Pass_TD_list.append(stats.text)
				elif(count == 3): INT_list.append(stats.text)
				elif(count == 4): RUSH_list.append(stats.text)
				elif(count == 5): Rush_YDS_list.append(stats.text)
				elif(count == 6): Pass_TD_list.append(stats.text)
				elif(count == 7): REC_list.append(stats.text)
				elif(count == 8): Rec_YDS_list.append(stats.text)
				elif(count == 9): Rec_TD_list.append(stats.text)
				elif(count == 10): PTS_list.append(stats.text)
				count += 1
		start_index += 40
		end_count += 6
		new_url = 'http://games.espn.com/ffl/tools/projections?&slotCategoryId='+position+'&seasonTotals=true&seasonId='+str(year)+'&startIndex='+str(start_index)
		r = urllib.request.urlopen(new_url)
		r = r.read()
		soup = BeautifulSoup(r, 'lxml')	
		print(new_url)
	position_list = [position_name] * len(player_list)
	output = zip(list(range(len(player_list))), player_list, position_list, CA_list, Pass_YDS_list, Pass_TD_list, INT_list, RUSH_list, Rush_YDS_list, Pass_TD_list, REC_list, Rec_YDS_list, Rec_TD_list, PTS_list)
	with open(position_name+'.csv',"w") as outfile:
		outfile.write("Rank,Player,Position,CA,Pass_YDS,Pass_TD,INT,RUSH,Rush_YDS,Pass_TD,REC,Rec_YDS,Rec_TD,PTS\n")
		for player in output:
			outfile.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(*player))
	pass

#Custom functions to scrape defense and kicking data statistics
def scrape_defense_data(year, position_name = 'd', position = D, player_list = [], TT_list = [], SCK_list = [], FF_list = [], FR_list = [], INT_list = [], ITD_list = [], FTD_list = [], PTS_list = []):
	start_index = 0
	base_url = 'http://games.espn.com/ffl/tools/projections?&seasonTotals=true&seasonId='+str(year)+'&slotCategoryId='+position
	r = urllib.request.urlopen(base_url)
	r = r.read()
	soup = BeautifulSoup(r, 'lxml')
	for player in soup.find_all('tr'):
		for player_name in player.find_all('a')[88:120]:
			if(player_name.text != '' and player_name.text != 'PTS'):
				player_list.append(player_name.text)
		count = 0
		for stats in player.find_all(class_ = 'playertableStat')[8:]:
			if(count == 8): count = 0
			if(count == 0): TT_list.append(stats.text)
			elif(count == 1): SCK_list.append(stats.text)
			elif(count == 2): FF_list.append(stats.text)
			elif(count == 3): FR_list.append(stats.text)
			elif(count == 4): INT_list.append(stats.text)
			elif(count == 5): ITD_list.append(stats.text)
			elif(count == 6): FTD_list.append(stats.text)
			elif(count == 7): PTS_list.append(stats.text)
			count += 1

	output = zip(list(range(len(player_list))), player_list, position_list, TT_list, SCK_list, FF_list, FR_list, INT_list, ITD_list, FTD_list, PTS_list)
	outfile = open(position_name+'.csv',"w")

	outfile.write("Rank,Player,Position,TT,SCK,FF,FR,INT,ITD,FTD,PTS\n")
	for player in output:
		outfile.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(*player))
	outfile.close()
	pass

def scrape_kicker_data(year, position_name = 'k', position = K, player_list = [], R1_list = [], R2_list = [], R3_list = [], TOT_list = [], XP_list = [], PTS_list = []):
	start_index = 0
	base_url = 'http://games.espn.com/ffl/tools/projections?&seasonTotals=true&seasonId='+str(year)+'&slotCategoryId='+position
	r = urllib.request.urlopen(base_url)
	r = r.read()
	soup = BeautifulSoup(r, 'lxml')
	for player in soup.find_all('tr'):
		for player_name in player.find_all('a')[82:119]:
			if(player_name.text != '' and player_name.text != 'PTS'):
				player_list.append(player_name.text)
		count = 0
		for stats in player.find_all(class_ = 'playertableStat')[6:-48]:
			if(count == 6): count = 0
			if(count == 0): R1_list.append(stats.text)
			elif(count == 1): R2_list.append(stats.text)
			elif(count == 2): R3_list.append(stats.text)
			elif(count == 3): TOT_list.append(stats.text)
			elif(count == 4): XP_list.append(stats.text)
			elif(count == 5): PTS_list.append(stats.text)
			count += 1
		for stats in player.find_all(class_ = 'playertableStat appliedPoints sortedCell')[:-8]:
			PTS_list.append(stats.text)

	output = zip(list(range(len(player_list))), player_list, position_list, R1_list, R2_list, R3_list, TOT_list, XP_list, PTS_list)
	outfile = open(position_name+'.csv',"w")

	outfile.write("Rank,Player,Position,R1,R2,R3,TOT,XP,PTS\n")
	for player in output:
		outfile.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(*player))
	outfile.close()
	pass
	

def main():
	#TODO: Figure out why I can only call 1 function at a time

	#scrape_position_data('qb', QB, 2017)	
	#scrape_position_data('rb', RB, 2017)
	#scrape_position_data('wr', WR, 2017)
	#scrape_position_data('te', TE, 2017)
	#scrape_defense_data(2017)
	#scrape_kicker_data(2017)

if __name__ == '__main__':
	main()