# Fantasy Football AutoDrafter

## REQUIREMENTS
- Python3
- sqlite browser

## Running
1. Clone or Download Repository

2.  Change to Directory

3.  Run the program: `python3 drafter.py`

## Auto-Drafting Strategy
- This program has 2 separate AI:

	1. Player 1: Drafts based on “Value Based Drafting”, a statistical methodology of ranking players based on their projected points compared to other players in their position.
	
	2. Players 2-8: Drafts based on the “Average Draft Position” of all players according to data from mock drafts and live drafts.
	
	- Manipulate code to manually draft your own team by commenting and removing comments around labeled class instances 


## Results

I added the cumulative fantasy points of each team’s starters (and backups/free agents if a starter became inactive) and gave each team a total score. This represents a quantified estimate of the team's performance.


![](https://github.com/shaeferd/FFDrafter/blob/master/Visualization/Team_Results.png?raw=true)

Player 1, using “Value Based Drafting”, had the 3rd highest score. Results are inconclusive given random error (injuries), statistical insignificance, and minimal trial numbers (only 1 season tested).

## Extra
![](https://github.com/shaeferd/FFDrafter/blob/master/Visualization/Scores_V_Projections.png?raw=true)

The projected scores seemed to be a pretty close match to actual scores aside from outliers


