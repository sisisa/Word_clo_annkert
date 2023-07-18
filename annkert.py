from wordcloud import WordCloud

wc = WordCloud(font_path='C:/Windows/Fonts/HGRSGU.TTC')

with open('annkert.txt', 'r', encoding='utf-8') as file:
    text = file.read()

wc.generate(text)
wc.to_file('annkert.png')
