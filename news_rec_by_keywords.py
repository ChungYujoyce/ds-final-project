

def news_recommend_keywords(item_id, num= 10):
    path_df = "Pickles/News_dataset.pickle"

    with open(path_df, 'rb') as data:
        df = pickle.load(data)