from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/'
pages = requests.get(url)

soup = BeautifulSoup(pages.content, 'html.parser')
tags = soup.find_all('div', class_="quote")

for tag in tags:
    text = tag.find('span', class_="text")
    person = tag.find('small', class_="author")

    ls = [text.text, person.text]
    print(ls)
