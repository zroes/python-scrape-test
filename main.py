import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)

quotes = []
authors = []
urls = [f"http://quotes.toscrape.com/page/{i}/" for i in range(1, 11)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content)

    quotes.extend([i.text for i in soup.find_all(class_='text')])
    authors.extend([i.text for i in soup.find_all(class_='author')])

for i in range(len(quotes)):
    print(authors[i])
    print(quotes[i])
