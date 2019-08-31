import requests
r = requests.get('https://news.yahoo.co.jp')
print(r.headers)
print("--------")
print(r.encoding)
print(r.content)

from bs4 import BeautifulSoup
html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"
soup = BeautifulSoup(html, "html.parser")
print(soup.select("h1"))
