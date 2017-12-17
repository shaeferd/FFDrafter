Fantasy Football AutoDrafter

Requirements: Python3, sqlite browser

Step 1: Download and Install

Step 2: Open terminal and change to the directory (FFDrafter)

Step 3: Run the program: “python3 drafter.py”

Explanation: This program has 2 separate AI: 

	1. Player 1 (Draft Class): drafts based on “Value Based Drafting”, a statistical methodology of ranking players based on their projected points compared to other players in their position.
	
	2. Players 2-8 (AutoDraft Class): Drafts based on the “Average Draft Position” of all players according to data from mock drafts and live drafts. (Date scraped from ESPN, NFL, and footballguys.com API)

Step 4: To see results of 2017 test, run “python3 results.py” or look below

Explanation: I added the cumulative fantasy points of each team’s starters (and backups/free agents if a starter became injured/inactive) and gave each team a total score.

Result:

(https://github.com/shaeferd/FFDrafter/tree/master/Visualization/Team_Results.png)

Player 1, using “Value Based Drafting”, had the 3rd highest score. Results are inconclusive given random error (injuries) and minimal trial numbers (only 1 season tested).

Extra:

![Projection Accuracy](https://github.com/shaeferd/FFDrafter/tree/master/Visualization/Scores_V_Projections.png)

To create a scatterplot of NFL Fantasy Football’s projected scores vs actual scores, run “python3 projections.py”. The projected scores seemed to be a pretty close match aside from outliers (mostly injured players)


TODO:

Make draft class in drafter 1 class

comment everything out

shorten stuff/make more efficient

fewer files
