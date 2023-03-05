from bs4 import BeautifulSoup

with open('emma.html', 'r') as emma_file:
    content = emma_file.read()
    
    soup = BeautifulSoup(content, 'lxml')

    #grabbing specific tags
    button_tag = soup.find('button')
    tag = soup.find_all('h1')
    
    for t in tag:
        print(button_tag.text + " for " + t.text)