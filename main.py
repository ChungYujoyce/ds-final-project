from flask import Flask, render_template, request, redirect, url_for
#from config import DevConfig
#from sentiment import get_all_words, get_tweets_for_model, remove_noise,process
#from datetime import timedelta
from news_word_cloud import process_cloud
from news_rec_by_keywords import news_recommend_keywords
#import requests
from news_rec_by_title import news_recommendation
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
 	return render_template('about.html')
@app.route('/classification')
def work():
    return render_template('classification.html')

query = ""
title = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "Blue", "Yellow", "Green", "Purple"]
score = [12, 19, 3, 5, 2, 3, 6, 8, 4, 9]
fig_name = "cloud_result/wordCloud.png"
count = 0
@app.route('/loading', methods=['GET','POST'])
def load():
    if request.method == 'POST':
        global query
        query = request.form.get('query')
        return render_template('loader.html')

@app.route('/news_process')
def process():
    global query, title, score
    print(query)

    if type(int(query)) == int:
        res = news_recommendation(query)
    else:
        res = news_recommend_keywords(query)
    for rec in recs:
        title.append(rec[1])
        score.append(rec[0])
    return render_template('rec.html', fig_name = str(fig_name), score=score, title=title)
    
@app.route('/news_recommend', methods=['GET','POST'])
def recommend():
    return render_template('rec.html', fig_name = str(fig_name), score=score, title=title)

@app.route('/features')
def products():
 	return render_template('features.html')

@app.route('/word_cloud', methods=['GET','POST'])
def word_cloud(): 
    if request.method == 'POST':
        global fig_name
        global count
        input_text = request.form.get('news')
        fig_name, font_path, count = process_cloud(input_text, count)
        print("count: ", count)
        return render_template('rec.html', fig_name = str(fig_name), score=score, title=title)
    else:
        return render_template('rec.html', fig_name = str(fig_name), score=score, title=title)

'''
@app.route('/sentiment', methods=['GET','POST'])
def sentiment():
    if request.method == 'POST':
        userinput = request.form.get('result')
        abc = requests.post('http://text-processing.com/api/sentiment/', data={"text": str(userinput)})
        obj = abc.json()
        if obj["label"] == "pos":
            backimg = "static/img/pos.jpg"
            font = "font-family: 'Princess Sofia', cursive;"
        elif obj["label"] == "neg":
            backimg = "static/img/sad.jpg"
            font = "font-family: 'Special Elite', cursive;"
        else:
            backimg = "static/img/neutral.jpg"
            font = "font-family: 'Balthazar', serif;"


        #obj = json.loads(str(abc.text)) ERROR
        # print(dump(abc))
        return render_template('result.html', A= str(userinput), B1=str(obj["probability"]["pos"]),B2=str(obj["probability"]["neutral"]),B3=str(obj["probability"]["neg"]),B4=str(obj["label"]), backimg = backimg, font=font)
        
    return render_template('sentiment.html')

'''

@app.route('/news_info')
def info():
    return render_template('news_info.html')


if __name__ == '__main__':
    app.debug = True
    app.run()