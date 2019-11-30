from operator import itemgetter
list_of_teams = [{} for i in range(4)]
list_of_teams[0]["name"] = "Iran"
list_of_teams[1]["name"] = "Spain"
list_of_teams[2]["name"] = "Portugal"
list_of_teams[3]["name"] = "Morocco"
game_schedule = [[i, j] for i in range(3) for j in range(i + 1, 4)]
for i in range(6):
    result = input()    
    result = result.split("-")    
    result = list(map(int, result))
    list_of_teams[game_schedule[i][0]]["goals_for"] = list_of_teams[game_schedule[i][0]].get("goals_for", 0) + result[0]    
    list_of_teams[game_schedule[i][0]]["goals_against"] = list_of_teams[game_schedule[i][0]].get("goals_against", 0) + result[1]    
    list_of_teams[game_schedule[i][1]]["goals_for"] = list_of_teams[game_schedule[i][1]].get("goals_for", 0) + result[1]    
    list_of_teams[game_schedule[i][1]]["goals_against"] = list_of_teams[game_schedule[i][1]].get("goals_against", 0) + result[0]    
    if result[0] > result[1]:
        list_of_teams[game_schedule[i][0]]["wins"] = list_of_teams[game_schedule[i][0]].get("wins", 0) + 1
        list_of_teams[game_schedule[i][1]]["wins"] = list_of_teams[game_schedule[i][1]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][1]]["losts"] = list_of_teams[game_schedule[i][1]].get("losts", 0) + 1
        list_of_teams[game_schedule[i][0]]["losts"] = list_of_teams[game_schedule[i][0]].get("losts", 0) + 0
        list_of_teams[game_schedule[i][0]]["draws"] = list_of_teams[game_schedule[i][0]].get("draws", 0) + 0
        list_of_teams[game_schedule[i][1]]["draws"] = list_of_teams[game_schedule[i][1]].get("draws", 0) + 0
    elif result[1] > result[0]:
        list_of_teams[game_schedule[i][1]]["wins"] = list_of_teams[game_schedule[i][1]].get("wins", 0) + 1
        list_of_teams[game_schedule[i][0]]["wins"] = list_of_teams[game_schedule[i][0]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][0]]["losts"] = list_of_teams[game_schedule[i][0]].get("losts", 0) + 1
        list_of_teams[game_schedule[i][1]]["losts"] = list_of_teams[game_schedule[i][1]].get("losts", 0) + 0
        list_of_teams[game_schedule[i][0]]["draws"] = list_of_teams[game_schedule[i][0]].get("draws", 0) + 0
        list_of_teams[game_schedule[i][1]]["draws"] = list_of_teams[game_schedule[i][1]].get("draws", 0) + 0
    else:
        list_of_teams[game_schedule[i][0]]["draws"] = list_of_teams[game_schedule[i][0]].get("draws", 0) + 1
        list_of_teams[game_schedule[i][1]]["draws"] = list_of_teams[game_schedule[i][1]].get("draws", 0) + 1
        list_of_teams[game_schedule[i][1]]["wins"] = list_of_teams[game_schedule[i][1]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][0]]["wins"] = list_of_teams[game_schedule[i][0]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][0]]["losts"] = list_of_teams[game_schedule[i][0]].get("losts", 0) + 0
        list_of_teams[game_schedule[i][1]]["losts"] = list_of_teams[game_schedule[i][1]].get("losts", 0) + 0
for team in list_of_teams:
    team["goal difference"] = team["goals_for"] - team["goals_against"]
    team["points"] = 3*team["wins"] + team["draws"]
list_of_teams = sorted(list_of_teams, key = itemgetter("points", "wins"), reverse = True)
team_points_and_wins = lambda x : (x["points"], x["wins"])
###### This part might be reduced ###
target_index = []
for i in range(3):
    if (team_points_and_wins(list_of_teams[i]) == team_points_and_wins(list_of_teams[i + 1])):
        target_index.append(i)
if target_index != []:
    part1 = list_of_teams[0 : target_index[0]]
    part2 = sorted(list_of_teams[target_index[0] : target_index[-1] + 2], key = itemgetter("name"))
    if (target_index[-1] + 2 < 4):
        part3 = list_of_teams[target_index[-1] + 2 : 5]
        list_of_teams = part1 + part2 + part3
    else:
        list_of_teams = part1 + part2
#####################################
for team in list_of_teams:
    print("%s  wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d" \
          % (team["name"], team["wins"], team["losts"], team["draws"], team["goal difference"], team["points"]))
