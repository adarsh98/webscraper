from bs4 import BeautifulSoup
import requests

url = "quotes.toscrape.com"
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")