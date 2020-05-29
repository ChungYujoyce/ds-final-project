import nltk,os
import requests
import pandas as pd
nltk.download('punkt')
import numpy as np
import pickle
from nltk.tokenize import word_tokenize
#!pip install -U gensim
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel
from gensim.similarities import MatrixSimilarity

def news_recommend_keywords(keywords, num=10):
    keywords = [word for word in keywords.split()]
    path_df = "Pickles/News_central_rec2.pickle"

    with open(path_df, 'rb') as data:
        df = pickle.load(data)

    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = []
        Words = ''
        for col in columns:
            if col == 'Content':
                words += row[col].split()  
        words = list(set(words))
        row['bag_of_words'] = words


    processed_keywords = df.bag_of_words.to_list()
    dictionary = Dictionary(processed_keywords) # create a dictionary of words from our keywords
    corpus = [dictionary.doc2bow(doc) for doc in processed_keywords] 
    #create corpus where the corpus is a bag of words for each document

    tfidf = TfidfModel(corpus) #create tfidf model of the corpus
    
    # Create the similarity data structure. This is the most important part where we get the similarities between the news.
    sims = MatrixSimilarity(tfidf[corpus], num_features=len(dictionary))
    query_doc_bow = dictionary.doc2bow(keywords) # get a bag of words from the query_doc
    query_doc_tfidf = tfidf[query_doc_bow] #convert the regular bag of words model to a tf-idf model where we have tuples
    # of the news ID and it's tf-idf value for the news

    similarity_array = sims[query_doc_tfidf] # get the array of similarity values between our news and every other news. 
    #So the length is the number of news we have. To do this, we pass our list of tf-idf tuples to sims.

    similarity_series = pd.Series(similarity_array.tolist(), index=df.Title.values) #Convert to a Series
    top_hits = similarity_series.sort_values(ascending=False)[:num] #get the top matching results, 
    # i.e. most similar news

    titles = []
    scores = []
    for idx, (title,score) in enumerate(zip(top_hits.index, top_hits)):
        #print("%d '%s' with a similarity score of %.3f" %(idx+1, title, score))
        titles.append(title)
        scores.append(score)
      
    return titles, scores
