from bs4 import BeautifulSoup
import requests
import json
import csv


url = "http://soccer.sportsopendata.net/v1/leagues/premier-league/seasons/16-17/teams" 
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

print(content) 