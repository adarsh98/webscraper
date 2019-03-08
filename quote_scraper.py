from bs4 import BeautifulSoup
from scrapely import Scraper
import requests
import json

'''quote_list = []

def scrape_func(content):
    try:
        quotes = content.find_all('span', attrs = {"class": "text"})
        authors = content.find_all('small', attrs = {"class": "author"})

        for i in range(len(quotes)):
            quote_obj = {"Quote": quotes[i].text, "Author": authors[i].text}
            quote_list.append(quote_obj)

    except AttributeError:
        print("Nonetype Attribute")

    except SyntaxError:
        print("Incorrect Syntax")

    except IndexError:
        print("Index Out of Range")

    except:
        print("Error Happened")


'''

url = "http://quotes.toscrape.com/"
response = requests.get(url) #option to add timeout
content = BeautifulSoup(response.content, "html.parser")

url1 = "http://quotes.toscrape.com/page/2/"
response1 = requests.get(url1)
content1 = BeautifulSoup(response1.content, "html.parser")

try:

    quotes = content.find_all('span', attrs = {"class": "text"})
    authors = content.find_all('small', attrs = {"class": "author"})

    quote_list = []

    for i in range(len(quotes)):
        quote_obj = {"Quote": quotes[i].text, "Author": authors[i].text}
        quote_list.append(quote_obj)
        '''print(quotes[i].text)
        print(authors[i].text)
        print('\n')'''


    quotes = content1.find_all('span', attrs= {"class": "text"})
    authors = content1.find_all('small', attrs= {"class": "author"})

    for j in range(len(quotes)):
        quote_obj = {"Quote": quotes[j].text, "Author": authors[j].text}
        quote_list.append(quote_obj) 

    with open('quotedata.json', 'w') as outfile:
        json.dump(quote_list, outfile)
        
except AttributeError:
    print("Nonetype Attribute")

except SyntaxError:
    print("Incorrect Syntax")

except IndexError:
    print("Index Out of Range")

except:
    print("Error Happened")
