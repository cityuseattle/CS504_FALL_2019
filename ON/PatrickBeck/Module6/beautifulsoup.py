import bs4
import requests

# file = open('example.html')
# lsoup = bs4.BeautifulSoup(file.read(), 'html.parser')
# elem = lsoup.select('#author')
# print(elem[0].get_text())

res = requests.get('http://www.cs.cmu.edu/~pausch/')
# used for display error message if url not valid
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#store list of all <h1> tags element
element = soup.select('h1')
for item in element:
    print(item)
    print(item.get_text())
    print()