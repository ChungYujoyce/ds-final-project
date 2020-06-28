import nltk,os
import requests
import pandas as pd
nltk.download('punkt')
import numpy as np
import pickle
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

    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(ds['Content'])
    #print(tfidf_matrix)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    results = {}

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

        results[row['id']] = similar_items[1:]

    recs = results[item_id][:num]
    titles = []
    scores = []
    for rec in recs:
        #print(rec)
        #print("Recommended: " + item(rec[1], ds) + " (score:" + str(rec[0]) + ")")
        #print(item(rec[1], ds))
        titles.append(item(rec[1], ds))
        scores.append(rec[0].item())
    #print(type(titles[0]), type(scores[1]))
    return titles, scores


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
    
def cosine_recommender(title, top=10):
    path_df = "Pickles/News_central_rec2.pickle"

    with open(path_df, 'rb') as data:
        df = pickle.load(data)
        
    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            if col == 'Content':
                words = words + row[col]+ ' '
        row['bag_of_words'] = words
    text = df.bag_of_words.tolist()
    #title = df.loc[count]['Title']
    vectorizer = CountVectorizer(text)
    vectors = vectorizer.fit_transform(text).toarray()
    df_index = title # set id as user input

    cosines = []
    for i in range(len(vectors)):
        vector_list = [vectors[df_index], vectors[i]]
        cosines.append(cosine_similarity(vector_list)[0,1])

    cosines = pd.Series(cosines)
    index = cosines.nlargest(top+1).index

    matches = df.loc[index]
    titles = []
    scores = []
    for title,score in zip(matches['Title'][1:],cosines[index][1:]):
        titles.append(title)
        scores.append(score)

    return titles, scores

def get_jaccard_sim(str1, str2):
    a = set(str1.split(','))
    b = set(str2.split(','))
    c = a.intersection(b)
    return(float(len(c)) / (len(a) + len(b) - len(c)))


def jaccard_recommender(title, number_of_hits=10):
    path_df = "Pickles/News_central_rec2.pickle"

    with open(path_df, 'rb') as data:
        df = pickle.load(data)

    dff = df[title]
    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            if col == 'Content':
                words = words + row[col]+ ' '
        row['bag_of_words'] = words
    keyword_string = dff.bag_of_words.iloc[0]

    jaccards = []
    for news in df['bag_of_words']:
        jaccards.append(get_jaccard_sim(keyword_string, news))
    jaccards = pd.Series(jaccards)
    jaccards_index = jaccards.nlargest(number_of_hits+1).index
    matches = df.loc[jaccards_index]
    return zip(matches['Title'][1:],jaccards[jaccards_index][1:]) 

#cosine_recommender(111)
        




