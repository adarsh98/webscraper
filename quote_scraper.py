from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url) #option to add timeout
content = BeautifulSoup(response.content, "html.parser")

try:
    '''for quote in content.find_all('span', attrs={"class": "text"}):
        print(quote.text,'\n') 
    
    for author in content.find_all('small', attrs={"class": "author"}):
        print(author.text)'''

    quotes = content.find_all('span', attrs = {"class": "text"})
    authors = content.find_all('small', attrs = {"class": "author"})

    for i in range(len(quotes)):
        print(quotes[i].text)
        print(authors[i].text)
        print('\n')
        
    '''for quote in content.find_all('span'):
        quote_content = quote.find(class_ = 'text').text
        print(quote_content)'''

except AttributeError:
    print("Nonetype Attribute")

except SyntaxError:
    print("Incorrect Syntax")

except:
    print("Error happened")
