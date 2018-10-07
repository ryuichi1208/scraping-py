# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
print title_tag

# タイトルを文字列を出力
print title
