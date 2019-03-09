import requests
import json

url = "http://soccer.sportsopendata.net/v1/leagues/premier-league/seasons/16-17/teams" 
response = requests.get(url)
code = response.status_code
if(code == 200 or code == 301):

    content = response.content.decode("utf-8")
    stuff = response.json()
    
    team_data = stuff['data']['teams']

    team_names = [li['name'] for li in team_data]

    team_foundation = [li['team_foundation'] for li in team_data]

    for i in range(len(team_names)):
        print(team_names[i], ":", team_foundation[i])  

    team_list = []
else:
    print(code)