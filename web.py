import webbrowser
import requests
from bs4 import BeautifulSoup

domain = 'https://www.imdb.com'
response = requests.get(domain)
page = BeautifulSoup(response.content, 'html.parser')

links = []
for url in page.find_all('a'):
    if 'marvel' in url.get_text().lower():
        webbrowser.open(domain + url.get('href'))


print(links)
