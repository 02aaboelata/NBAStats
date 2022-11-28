import requests
import json

active = True
while(active == True):   
    player1 = input("Enter first player: ")
    p1_list = json.loads(requests.get ("https://www.balldontlie.io/api/v1/players?search=" + player1).text)["data"]
    if (len(p1_list) > 1):
        for i in range(len(p1_list)):
            print(i + 1, ": ", p1_list[i]["first_name"], p1_list[i]["last_name"])
        p1_select = int(input("Which player?: "))
        if (p1_select < 1 or p1_select > len(p1_list)):
            exit("Invalid selection")
        else:
            p1_profile = p1_list[p1_select - 1]
    else: 
        p1_profile = p1_list[0]


    player2 = input("Enter second player: ")
    p2_list = json.loads(requests.get ("https://www.balldontlie.io/api/v1/players?search=" + player2).text)["data"]
    if (len(p2_list) > 1):
        for i in range(len(p2_list)):
            print(i + 1, ": ", p2_list[i]["first_name"], p2_list[i]["last_name"])
        p2_select = int(input("Which player?: "))
        if (p2_select < 1 or p2_select > len(p2_list)):
            print("Invalid selection")
        else:
            p2_profile = p2_list[p2_select - 1]
    else: 
        p2_profile = p2_list[0]

    p1_id = p1_profile["id"]
    p2_id = p2_profile["id"]
    
    season = input("Current season (enter) or select season to compare: ")
    if (season == ''):
        season = "2021"

    p1_stats = json.loads(requests.get ("https://www.balldontlie.io/api/v1/season_averages?season=" + 
        season + "&player_ids[]=" + str(p1_id)).text)["data"][0]

    p2_stats = json.loads(requests.get ("https://www.balldontlie.io/api/v1/season_averages?season=" + 
        season + "&player_ids[]=" + str(p2_id)).text)["data"][0]
    
    print('')
    categ = input("Show all stats (enter) or choose a specific category?: ")  

    if (categ == ''):
        for k in p1_stats:
            if (k != "player_id" and k != "season"):
                print(k + ": ")
                print(p1_profile["first_name"], p1_profile["last_name"] + ":", (p1_stats)[k])
                print(p2_profile["first_name"], p2_profile["last_name"] + ":", (p2_stats)[k], '\n')

    else:
        print(categ + ": ")
        print (p1_profile["first_name"], p1_profile["last_name"] + ":", p1_stats[categ])
        print (p2_profile["first_name"], p2_profile["last_name"] + ":", p2_stats[categ])
    
    cont = input("Compare again? y/n: ")
    if (cont.lower() == "yes" or cont.lower() == "y"):
        active = True
    else: 
        active = False
