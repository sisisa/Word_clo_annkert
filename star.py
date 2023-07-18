from wordcloud import WordCloud

wc = WordCloud(font_path='C:/Windows/Fonts/HGRSGU.TTC')

with open('star.txt', 'r', encoding='utf-8') as file:
    text = file.read()

wc.generate(text)
wc.to_file('wordcloud.png')
