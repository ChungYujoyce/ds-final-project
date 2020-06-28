import pandas as pd
from collections import defaultdict
import csv
import matplotlib.pyplot as plt

"""
Plotting the average tweets of specific politicians which are of key interst, hence we form a list of politicians
"""
def average_tweets(twitter_handles=None,politician=None):
    ''' 
    This function plots a histogram of the average tweets per day of various politicians.
    :param twitter_handles: The list of the data files of politicians to be analysed
    :param politician: The list of names of the politicians to be analysed
    :return: a dictionary containing the average number of daily tweets per politician
    '''
    assert isinstance(twitter_handles, list)
    assert isinstance(politician, list)
    
    average_tweet=defaultdict(float)
    for p in range(len(politician)):
        per_day=defaultdict(int)
        data=pd.read_csv('data/' + twitter_handles[p])
        date=data['Date Created']
        for d in date:
            per_day[d]+=1
        avg=sum(per_day.values())/len(per_day.keys())
        average_tweet[politician[p]]=avg
    key = list(average_tweet.keys())
    value = list(average_tweet.values())
    
    return key, value
    

