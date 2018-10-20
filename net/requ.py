# encoding UTF-8
import requests

# 取得するURL
url_top = "https://www.sejuku.net/blog/"

response = requests.get(url_top)
response.encoding = response.apparent_encoding

response_html = response.text


with open('result.html', 'w', encoding='utf-8') as f:
    f.write(response_html)

print('save file')
