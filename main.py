from flask import Flask, render_template, request, redirect, url_for
#from config import DevConfig
#from sentiment import get_all_words, get_tweets_for_model, remove_noise,process
#from datetime import timedelta
from news_word_cloud import process_cloud
from news_rec_by_keywords import news_recommend_keywords
#import requests
from news_rec_by_title import news_recommendation, cosine_recommender
import pickle
import nltk
import json
from average_tweets import average_tweets
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

stop_words = ['President','Trump','Donald','and','want','need','they','This']
global stage
stage = 0
global year
year = 0 #all

global values
values = []
global labels
labels = []
global legend
legend = []

global fc_values
fc_values = []
global fc_legend

global rc_values
rc_values = []
global rc_legend

@app.route('/twitter')
def home_page():
    global values
    global labels
    global legend
    global fc_values
    global fc_legend
    global rc_values
    global rc_legend
    rc_values = []
    fc_values = []
    values = []
    labels = []
    try:
        data_file = "static/sen_data/sen_condensed_all.json"
        legend = 'All Years Sentiment Analysis'
        global year
        if year!=0:
            for i in range(2009, 2021):
                if year==i:
                    data_file = "static/sen_data/sen_condensed_" + str(year) + ".json"
                    legend = str(year) + ' Sentiment Analysis'
        with open(data_file) as json_file:
            sen_json = json.load(json_file)
            for sen in sen_json[:]:
                labels.append(str(sen['time']))
                values.append(float(sen['weight']))
    except Exception as e:
        print("Error : "+ e)
    
    try:
        data_file = "static/fc_data/fc_condensed_all.json"
        fc_legend = 'All Years Favorite Count'
        if year!=0:
            for i in range(2009, 2021):
                if year==i:
                    data_file = "static/fc_data/fc_condensed_" + str(year) + ".json"
                    fc_legend = str(year) + ' Favorite Count'
        with open(data_file) as json_file:
            fc_json = json.load(json_file)
            for fc in fc_json[:]:
                fc_values.append(float(fc['weight']))
    except Exception as e:
        print("Error : "+ e)
    
    try:
        data_file = "static/rc_data/rc_condensed_all.json"
        rc_legend = 'All Years Retweet Count'
        if year!=0:
            for i in range(2009, 2021):
                if year==i:
                    data_file = "static/rc_data/rc_condensed_" + str(year) + ".json"
                    rc_legend = str(year) + ' Retweet Count'
        with open(data_file) as json_file:
            rc_json = json.load(json_file)
            for rc in rc_json[:]:
                rc_values.append(float(rc['weight']))
                #print(sen)
                #print(sen['time'])
    except Exception as e:
        print("Error : "+ e)
    #return render_template('twitter.html', stop_words = stop_words, values=values, labels=labels, legend=legend)
    return render_template('twitter.html', stop_words = stop_words, values=values, labels=labels, legend=legend, rc_values=rc_values, rc_legend=rc_legend,fc_values=fc_values, fc_legend=fc_legend)
@app.route('/reset')
def reset():
    global stage
    stage = 0
    try:
        stop_words.pop(len(stop_words)-1)
    except Exception as e:
        pass
    print(stop_words)
    return redirect('/twitter')

@app.route('/noun')
def noun():
    global stage
    stage = 1
    return redirect('/twitter')

@app.route('/twitter', methods=['POST'])
def my_form_post():
    text = request.form.get('stop_words', None)
    stop_words.append(text)
    return render_template('twitter.html', stop_words = stop_words)

@app.route('/twitter_word_cloud', methods=['GET']) #all
def twitter_word_cloud():
    try:
        global year
        data_file = "static/wordcloud_data/fre_condensed_all.json"
        if year!=0:
            for i in range(2009, 2021):
                if year==i:
                    data_file = "static/wordcloud_data/fre_condensed_" + str(year) + ".json"
        print(data_file)
        with open(data_file) as json_file:
            words_json = json.load(json_file)
            for words in words_json[:]:
                global stage
                #print(stage)
                if stage == 1:
                    #print(nltk.pos_tag([words['text']])[0][1])
                    if (not nltk.pos_tag([words['text']])[0][1].startswith('NNP') and words['text']!="Coronavirus"):
                        words_json.remove(words)
                    elif words['text'] in stop_words:
                        words_json.remove(words)
                else:
                    if words['text'] in stop_words:
                        words_json.remove(words)
        return json.dumps(words_json)
    except Exception as e:
        return '[]'

#----------------change year
@app.route('/all')
def all():
    global year
    year = 0
    return redirect('/twitter')
@app.route('/2020')
def _2020():
    global year
    year = 2020
    return redirect('/twitter')
@app.route('/2019')
def _2019():
    global year
    year = 2019
    return redirect('/twitter')
@app.route('/2018')
def _2018():
    global year
    year = 2018
    return redirect('/twitter')
@app.route('/2017')
def _2017():
    global year
    year = 2017
    return redirect('/twitter')
@app.route('/2016')
def _2016():
    global year
    year = 2016
    return redirect('/twitter')
@app.route('/2015')
def _2015():
    global year
    year = 2015
    return redirect('/twitter')
@app.route('/2014')
def _2014():
    global year
    year = 2014
    return redirect('/twitter')
@app.route('/2013')
def _2013():
    global year
    year = 2013
    return redirect('/twitter')
@app.route('/2012')
def _2012():
    global year
    year = 2012
    return redirect('/twitter')
@app.route('/2011')
def _2011():
    global year
    year = 2011
    return redirect('/twitter')
@app.route('/2010')
def _2010():
    global year
    year = 2010
    return redirect('/twitter')
@app.route('/2009')
def _2009():
    global year
    year = 2009
    return redirect('/twitter')
#---------------------------

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

@app.route('/political', methods=['GET', 'POST'])
def political():
    twitter_handles=['tedcruz_tweets.csv','BarackObama_tweets.csv','HillaryClinton_tweets.csv','JebBush_tweets.csv','KamalaHarris_tweets.csv','RandPaul_tweets.csv','realDonaldTrump_tweets.csv','SenSanders_tweets.csv','SenWarren_tweets.csv']
    politician=['Ted Cruz','Barack Obama','Hillary Clinton','Jeb Bush','Kamala Harris','Rand Paul', 'Donald Trump','Bernie Sanders','Elizabeth Warren']
    keys, values = average_tweets(twitter_handles,politician)
    return render_template('political.html', keys=keys, values=values)


if __name__ == '__main__':
    app.debug = True
    app.run()