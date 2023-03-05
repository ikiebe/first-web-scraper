from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/?'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('ol', class_='row')

for list in lists:
    title = list.find('a', href='catalogue/tipping-the-velvet_999/index.html')
    price = list.find('p', class_='price_color')

    l = [title.text, price.text]
    print(l)