from flask import Flask, render_template, request, redirect, url_for
#from config import DevConfig
#from sentiment import get_all_words, get_tweets_for_model, remove_noise,process
#from datetime import timedelta
from news_word_cloud import process_cloud
from news_rec_by_keywords import news_recommend_keywords
#import requests
from news_rec_by_title import news_recommendation, cosine_recommender
app = Flask(__name__)
import main_cloud
import main_political
import pickle

query = ""
title = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "Blue", "Yellow", "Green", "Purple"]
score = [12, 19, 3, 5, 2, 3, 6, 8, 4, 9]
title2 = ["b", "Blue", "Yellow", "Green", "Purple", "Orange", "Blue", "Yellow", "Green", "Purple"]
score2 = [2, 3, 6, 8, 4, 9, 12, 19, 3, 5]
title3 = ["a", "Blue", "Yellow", "Green", "Purple", "Orange", "Blue", "Yellow", "Green", "Purple"]
score3 = [1, 19, 3, 5, 2, 3, 6, 8, 4, 9]
fig_name = "cloud_result/wordCloud.png"
count = 0
model_type = 'Model 1'
model = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/classification')
def work():
    return render_template('classification.html')

@app.route('/news_info')
def info():
    return render_template('news_info.html')

@app.route('/loading', methods=['GET','POST'])
def load():
    if request.method == 'POST':
        global query
        global model_type
        query = request.form.get('query')
        model_type = request.form.get("selectmodel")
        return render_template('loader.html')

@app.route('/news_process')
def process():
    global query
    global model_type
    global title , title2, title3
    global score , score2, score3
    print(query)
    print(model_type)
    if model_type == 'Model 1':
        model = 0
    elif model_type == 'Model 2':
        model = 1
    else:
        model = 2
    if query.isnumeric():
        if model == 0:
            print("model 1")
            title, score = news_recommendation(int(query))
        elif model == 1:
            print("model 2")
            title2, score2 = cosine_recommender(int(query))
        else:
            print("model select wrong.")
    else:
        print("model 3")
        title3, score3 = news_recommend_keywords(query)
    return render_template('rec.html', fig_name = str(fig_name), score=score, title=title,\
    score2=score2, title2=title2, score3=score3, title3=title3,\
    data= [{'name':'Model 1'}, {'name':'Model 2'}, {'name':'Model 3'}])
    
@app.route('/news_recommend', methods=['GET','POST'])
def recommend():
    return render_template('rec.html', fig_name = str(fig_name), score=score, title=title,\
    score2=score2, title2=title2, score3=score3, title3=title3,\
    data= [{'name':'Model 1'}, {'name':'Model 2'}, {'name':'Model 3'}])

@app.route('/word_cloud', methods=['GET','POST'])
def word_cloud(): 
    if request.method == 'POST':
        global fig_name
        global count
        input_text = request.form.get('news')
        fig_name, font_path, count = process_cloud(input_text, count)
        print("count: ", count)
        return render_template('rec.html', fig_name = str(fig_name), score=score, title=title,\
    score2=score2, title2=title2, score3=score3, title3=title3,\
    data= [{'name':'Model 1'}, {'name':'Model 2'}, {'name':'Model 3'}])
        
    else:
        return render_template('rec.html', fig_name = str(fig_name), score=score, title=title,\
    score2=score2, title2=title2, score3=score3, title3=title3, \
    data= [{'name':'Model 1'}, {'name':'Model 2'}, {'name':'Model 3'}])

if __name__ == '__main__':
    app.debug = True
    app.run()