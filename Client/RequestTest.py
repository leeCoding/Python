
import requests
from bs4 import BeautifulSoup

url = 'http://www.santostang.com/'
p = requests.get(url)
print(p.text)
soup = BeautifulSoup(p.text,"lxml")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)