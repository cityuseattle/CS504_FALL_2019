import bs4
import requests

# file = open('example.html')
# lsoup = bs4.BeautifulSoup(file.read(), 'html.parser')
# elem = lsoup.select('#author')
# print(elem[0].get_text())

res = requests.get('http://www.cs.cmu.edu/~pausch/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
element = soup.select('h1')
for item in element:
    print(item)
    print(item.get_text())
    print()