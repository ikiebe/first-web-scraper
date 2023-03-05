from bs4 import BeautifulSoup
from colorama import Fore

print(Fore.GREEN + "Welcome to Emmanuel Web scraper")
inp = input("Enter the name of your file here: ")

with open(inp, 'r') as emma:
    content = emma.read()

    #creating a soup
    soup = BeautifulSoup(content, 'lxml')

    #getting specific tags
    tags = soup.find_all('h1')
    
    for tag in tags:
        print(tag.text)