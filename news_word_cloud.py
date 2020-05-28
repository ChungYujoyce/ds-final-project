import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = list(stopwords.words('english'))
import random

def process_cloud(text, count):
    NUMBER_OF_GENRE = 8
    fonts = [
        'Gloucester-MT-Extra-Condensed.ttf',
        'Cooper-Black.ttf',
        'Harlow-Solid-Italic.ttf',
        'Broadway.ttf',
        'Brush-Script-MT-Italic.ttf',
        'Gill-Sans-Ultra-Bold.ttf',
        'CopperplateGothicBold.ttf',
        'Wide-Latin.ttf',
    ] # genre[i] goes with fonts[i]

    font_path = os.getcwd() + "/static/assets/" + fonts[count]
    #background_image_path = os.getcwd() + "/assets/" + genres[j] + ".JPG"
    #background = "assets/" + genres[j] + ".JPG"

    nltk_stopwords = stopwords.words('english')
    customized_stopwords = ["the","and","i", "'s", "-", "--", "---", "n't", "'in", "``", "`", "'", "''", "'ll", "'ve"]
    Stopwords = customized_stopwords + nltk_stopwords + list(STOPWORDS)


    #input_text = open("./dataset/central/txt_file/elec_22.txt", "r").read()
    for stop_word in stop_words:
        regex_stopword = r"\b" + stop_word + r"\b"
    words = text.replace(regex_stopword, '')
    words = text.split()
    #print(words.count('china') , words.count('trump'))
    if words.count('china') > words.count('trump'):
        mask = os.getcwd() + "/static/assets/mask.jpg"
    elif words.count('china') < words.count('trump'):
        mask = os.getcwd() + "/static/assets/trump.png"
    else:
        mask = os.getcwd() + "/static/assets/virus.jpg"
    maskArray = np.array(Image.open(mask))
        
    word = WordCloud(stopwords = Stopwords, width = 2000, height = 1500,\
                     font_path = font_path, min_font_size = 3, max_font_size = 400, max_words = 200,\
                     background_color = "rgba(255, 255, 255, 0)",  mask = maskArray, \
                     mode = 'RGBA', colormap = plt.get_cmap('nipy_spectral') # nipy_spectral, tab10
           ).generate(text)
    fig_name = "cloud_result/wordCloud_"+str(count)+".png"
    word.to_file("./static/cloud_result/wordCloud_"+str(count)+".png")
    count += 1
    if(count == 8):
        count = 0
    return fig_name, font_path, count
