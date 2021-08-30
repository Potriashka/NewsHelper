from bs4 import BeautifulSoup
import requests
from main import SearchResults

# for every site in a list we'll do the search
for i in range(len(SearchResults)):
    url = SearchResults[i] # take the url of a site
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    thing = soup.find('h1')

    print(thing.text)
    i += 1