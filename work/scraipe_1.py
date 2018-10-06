# coding: UTF-8
from bs4 import BeautifulSoup
import urllib.request, urllib.error

# アクセスするURL
url = "https://www.nikkei.com/markets/kabu/"

# URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
#instance = urllib2.urlopen(url)
instance = urllib.request.urlopen(url=url)

# instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(instance, "html.parser")

# CSSセレクターを使って指定した場所のtextを表示します
print (soup.select_one("#CONTENTS_MARROW > div.mk-top_stock_average.cmn-clearfix > div.cmn-clearfix > div.mkc-guidepost > div.mkc-prices > span.mkc-stock_prices").text)
