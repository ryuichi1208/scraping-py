from bs4 import BeautifulSoup

r = requests.get("https://news.yahoo.co.jp/")

soup = BeautifulSoup(r.content, "html.parser")

print(soup.select("p.ttl"))
