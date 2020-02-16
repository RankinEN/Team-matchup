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
    while list_length > 0:
        selection = random.randint(0, (list_length - 1))
        team_one = teamList.pop(selection)
        list_length = len(teamList)
        selection = random.randint(0, (list_length - 1))
        team_two = teamList.pop(selection)
        list_length = len(teamList)
        matchups.append(team_one + " vs " + team_two)
        isWinner(team_one, team_two)
    return(matchups)

def isWinner(teamOne, teamTwo):
    print("This match is", teamOne, "VS", teamTwo + "!")
    scoreOne = random.randint(1,100)
    scoreTwo = random.randint(1,100)
    print(teamOne, "scored ", scoreOne, "points.")
    print(teamTwo, "scored", scoreTwo, "points.")
    if scoreOne > scoreTwo:
        print(teamOne, "wins the fight!")
    else:
        if scoreTwo > scoreOne:
            print(teamTwo, "wins the fight!")
        else:
            print("it was a tie!")


#main

teams_list = teams()
team_matchups = roster(teams_list)

for x in team_matchups:
    print(x)
