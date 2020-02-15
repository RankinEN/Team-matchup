#this program is intended to take in information and spit out who would win in a fight
#copyright Elizabeth Rankin

#import statements
import random

#def statments
def teams():
    team_list = []
    teamAdded = ""
    while teamAdded != "x":
        teamAdded = input("Write the team you want to add to the list here, enter 'x' to end team add: ")
        team_list.append(teamAdded)
    team_list.remove("x")
    return(team_list)

def roster(teamList):
    list_length = len(teamList)
    matchups = []
    while list_length >= 0:
        selection = random.randint(0, list_length)
        team_one = teamList[selection]
        del teamList[selection]
        list_length = len(teamList)
        selection = random.randint(0, list_length)
        team_two = teamList[selection]
        del teamList[selection]
        list_length = len(teamList)
        matchups.append(team_one + " vs " + team_two)
    return(matchups)



#main

teams_list = teams()
team_matchups = roster(teams_list)

for x in team_matchups:
    print(x)