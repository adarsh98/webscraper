from bs4 import BeautifulSoup
from scrapely import Scraper
import requests
import json

quote_list = []

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


def main():

    for i in range(1,11):
        url = "http://quotes.toscrape.com/page/" + str(i) + "/"
        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")
        scrape_func(content)
        with open('quotedata.json', 'w') as outfile:
            json.dump(quote_list, outfile)
     
    '''url = "http://quotes.toscrape.com/"
    response = requests.get(url) #option to add timeout
    content = BeautifulSoup(response.content, "html.parser")

    url1 = "http://quotes.toscrape.com/page/2/"
    response1 = requests.get(url1)
    content1 = BeautifulSoup(response1.content, "html.parser")

    url2 = "http://quotes.toscrape.com/page/3/"
    response2 = requests.get(url2)
    content2 = BeautifulSoup(response2.content, "html.parser")

    scrape_func(content)
    scrape_func(content1)
    scrape_func(content2)

    with open('quotedata.json', 'w') as outfile:
        json.dump(quote_list, outfile)'''
main()
        