import feedparser
import csv

# ホットエントリRSSの取得、解析
# 「総合」 RSS_URL = "http://b.hatena.ne.jp/hotentry.rss"
it = "http://b.hatena.ne.jp/hotentry/it.rss"
manabi = "http://b.hatena.ne.jp/hotentry/knowledge.rss"
kurashi = "http://b.hatena.ne.jp/hotentry/life.rss"
yononaka = "http://b.hatena.ne.jp/hotentry/social.rss"

# レスポンス
rss = [it, manabi, kurashi, yononaka]

hotentry = []

# はてブ数、タイトル、リンクを格納
for n in rss:
    hatebu_dic = feedparser.parse(n)

    for x in hatebu_dic.entries:
        hbm_count = x.hatena_bookmarkcount
        title = x.title
        link = x.link

        hotentry.append((hbm_count, title, link ))

# はてブ数でソート
hotentry = sorted(hotentry, key=lambda x:int(x[0]), reverse=True)

# 確認用に表示
for x in hotentry:
    print('{} || {} \n {}'.format(x[0], x[1], x[2]))

# csvに出力
f = open('hatebu_rss.csv', 'w', encoding='CP932', errors='ignore')
writer = csv.writer(f, lineterminator='\n')

for x in hotentry:
    writer.writerow(x)

f.close()
