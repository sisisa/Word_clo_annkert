from wordcloud import WordCloud
import os

# テキストファイル読み込み
f = open(os.path.sep.join(['corpora', 'en.txt']), encoding='utf-8')
raw = f.read()
f.close()
# print(raw)

#英文のワードクラウドを作成
wc = WordCloud().generate(raw)
wc.to_file("wc-2.png")

wc2 = WordCloud(max_font_size=36).generate(raw)
wc2.to_file("wc-3.png")