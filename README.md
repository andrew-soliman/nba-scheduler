# nba-scheduler

Overview

* Wrote a Python script that creates an optimized "NBA" schedule for any number of teams in a given league of competitors.
* Although a basketball season schedule is one use case of the the script, it can easily be modified to greatly simplify many other tasks, including settting up meetings with colleagues that have varying availability, etc.

Dependencies

* pandas, itertools, random
* Fun team names! XD

Design

* The script first takes in dicts of each team in the league, with the dicts including the team's name and all the time slots on each day of the week (M-F) on which they can play a match.
* Then, using itertools (Python package), the script pairs up each team in the league for the various matchups throughout the season, with each team playing each of the other teams once.
* Afterwards, the script utilzes pandas (Python package) to create an empty DataFrame that will be used to sleekly display the finalized schedule.
* Then, the various match-ups are run through an algorithm that scans for all the available times that overlap in either team's availability.
* If two teams have an overlap in multiple timeslots in any given weekday, or multiple weekdays in which they're both able to play, the script utilizes random (Python package) to select a timeslot at random.
* Once a timeslot has been decided, the script refers to the DataFrame, scanning for entries of either team in a given "Week" of the league's games.
* If the script cannot find an entry for either team in a given week, the script will determine that the week of the given matchup is one after the last week either team played. 
* The script utilizes the day of the week from the scanning algorithm, as well as the given week, to return the date of the match.

* The script finally neatly uploads all the acquired variables into the DataFrame.
* The script then iterates through the entire process for every matchup made for the season.

* The script ultimately displays the finalized NBA season schedule (pandas DataFrame) in the terminal.

Project Schedule

* Started: Wednesday October 5, 2022
* Completed: Saturday, October 9, 2022
