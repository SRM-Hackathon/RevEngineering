import pickle
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import difflib
import types
import string 


idx = 0

with open("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/cosine.pkl",'rb') as f:
    cosine_sim = pickle.load(f)
with open("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/index.pkl",'rb') as f:
    indices = pickle.load(f)
with open("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/title.pkl",'rb') as f:
    titles = pickle.load(f)
with open("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/md.pkl",'rb') as f:
    gen_md = pickle.load(f)

df = pd.DataFrame({'title':indices.index, 'index':indices.values})
df['title'] = df['title'].str.lower()
df['title'] = df['title'].str.replace('[{}]'.format(string.punctuation), '')

##

tit2id = {}
for index, row in df.iterrows():
    tit2id[row['title']] = row['index']

##

def contains(x,y):
    if difflib.SequenceMatcher(None,x,y).ratio() > 0.7:
        return True
    return False

##




def get_recommendations(title):
#     title = title.replace('[{}]'.format(string.punctuation), '')
#     title = title.lower()
    try:
        idx = int(indices[title])   
        if isinstance(idx, int):
            print(1)
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:31]
            movie_indices = [i[0] for i in sim_scores]
            return titles.iloc[movie_indices]
        elif isinstance(idx,pd.Series):
            print(2)
            idx = idx.values[0]
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:31]
            movie_indices = [i[0] for i in sim_scores]
            return titles.iloc[movie_indices]
        else:
            idx = 0
#             print(3)
#             print("Not Available. Searching for best fit.")
            try:
                idx = tit2id[title]
            except:
                #only for if no match  
                for index, row in df.iterrows():
                    title = title.replace('[{}]'.format(string.punctuation), '')
                    title = title.lower()
                    if contains(row['title'],title):
                        print(row['title'])
                        idx = row['index']
                        break
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:31]
            movie_indices = [i[0] for i in sim_scores]
            return titles.iloc[movie_indices]
    
    
    except:
        idx = 0
#        
        #only for if no match  
        for index, row in df.iterrows():
            title = title.replace('[{}]'.format(string.punctuation), '')
            title = title.lower()
            if contains(row['title'],title):
                print(row['title'])
                idx = row['index']
                break
            
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]


        movie = titles.iloc[movie_indices]
        dfnew = pd.DataFrame({'index':movie.index, 'list':movie.values})
        getlist = dfnew['list'].tolist()
        return(getlist[0:5])


def build_chart(genre, percentile=0.85):
    df = gen_md[gen_md['genre'] == genre]
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)
    
    return qualified

print(get_recommendations("Colonia"))