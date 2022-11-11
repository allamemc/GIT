from bs4 import BeautifulSoup
import requests

web='https://valeriemoreau.com/'
pagina=requests.get(web)
soup = BeautifulSoup(pagina.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))