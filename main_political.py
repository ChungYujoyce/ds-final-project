from main import app
from flask import Flask,request,render_template,redirect,url_for
import nltk
import json
from average_tweets import average_tweets

@app.route('/political', methods=['GET', 'POST'])
def political():
    twitter_handles=['tedcruz_tweets.csv','BarackObama_tweets.csv','HillaryClinton_tweets.csv','JebBush_tweets.csv','KamalaHarris_tweets.csv','RandPaul_tweets.csv','realDonaldTrump_tweets.csv','SenSanders_tweets.csv','SenWarren_tweets.csv']
    politician=['Ted Cruz','Barack Obama','Hillary Clinton','Jeb Bush','Kamala Harris','Rand Paul', 'Donald Trump','Bernie Sanders','Elizabeth Warren']
    keys, values = average_tweets(twitter_handles,politician)
    return render_template('political.html', keys=keys, values=values)




