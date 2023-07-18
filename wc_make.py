from wordcloud import WordCloud

wc = WordCloud(font_path='C:/Windows/Fonts/HGRSGU.TTC')
wc.read_file('star.txt')
wc.create('wordcloud.png',['根幹','初代'])

