import requests
import json
import urllib3
from bs4 import BeautifulSoup

with open('crimepage.html') as page:
    soup = BeautifulSoup(page, 'html.parser')
    for a in soup.find_all('a'):
        if 'class="text"' in str(a):
            url = a['href']
            res = requests.get(url)
            data = res.content.decode('utf8')

            f = open('allheros.txt', 'a+')

            for line in data.split('\n'):
                print(data)
                f.write(data)

            f.close()