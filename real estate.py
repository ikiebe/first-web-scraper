from bs4 import BeautifulSoup
import requests

url = 'https://www.pararius.com/apartments/amsterdam'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
tags = soup.find_all('section', class_='listing-search-item')

for tag in tags:
    title = tag.find("a", class_="listing-search-item__link--title")
    location = tag.find("div", class_="listing-search-item__sub-title'")
    price = tag.find("div", class_="listing-search-item__price")
    area = tag.find("li", class_="illustrated-features__item--surface-area")
    
    info = [title,location,price,area]
    
    print(info)
