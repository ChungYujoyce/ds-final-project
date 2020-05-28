import nltk,os
import requests
import pandas as pd
nltk.download('punkt')
import numpy as np
import pickle, time
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def item(id, ds):
    return ds.loc[ds['id'] == id]['Title'].tolist()[0].split('_')[0]

def news_recommendation(item_id, num= 10):
    path_df = "Pickles/News_dataset.pickle"

    with open(path_df, 'rb') as data:
        ds = pickle.load(data)
        
    ids  = [i for i in range(len(ds))]
    ids = pd.DataFrame(ids)
    ids.columns = ['id']
    ds = pd.concat([ds, ids],axis=1)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    start = time.time()
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(ds['Content'])
    print(tfidf_matrix)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    results = {}

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

        results[row['id']] = similar_items[1:]
        
    print('done!')
    # Just reads the results out of the dictionary.

    print("Recommending " + str(num) + " news similar to " + item(item_id, ds) + "...")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:
        print("Recommended: " + item(rec[1], ds) + " (score:" + str(rec[0]) + ")")

    current_time = now.strftime("%H:%M:%S")
    print("Finish tfidf processing at", current_time)
    spent = time.time() - start
    print("\nTotal spent time: "+str(spent) +"sec\n")
    return res




