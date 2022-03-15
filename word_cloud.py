import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

import sys , os

import wordcloud
os.chdir(sys.path[0])

text = open('text.txt' , mode = 'r' , encoding = 'utf-8').read()

stopword = STOPWORDS

wc = WordCloud(background_color = 'white' , max_words = 2000 , stopwords = stopword , max_font_size = 540 , random_state = 542 , height = 1080 , width = 1920)

wc.generate(text)

wc.to_file('wordcloud.png')



