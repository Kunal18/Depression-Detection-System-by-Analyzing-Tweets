# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:16:51 2019

@author: Mrunal Jayesh
"""
def predict(tweet):
    ###########################################################################
    ###########################################################################
    
    import utils
    import random
    import numpy as np
    from sklearn.naive_bayes import MultinomialNB
    from sklearn import svm
    from scipy.sparse import lil_matrix
    from sklearn.feature_extraction.text import TfidfTransformer
    import single_pre as s
    import pickle as pk
    
    UNIGRAM_SIZE = 15000
    VOCAB_SIZE = UNIGRAM_SIZE
    USE_BIGRAMS = True
    if USE_BIGRAMS:
        BIGRAM_SIZE = 10000
        VOCAB_SIZE = UNIGRAM_SIZE + BIGRAM_SIZE
    FEAT_TYPE = 'frequency'
    
    unigrams = pk.load(open("unigrams.pkl","rb"))
    bigrams = pk.load(open("bigrams.pkl","rb"))
    tfidf = pk.load(open("tfidf.pkl","rb"))
    clf = pk.load(open("clf.pkl","rb"))
    clf1 = pk.load(open("clf1.pkl","rb"))
    
    def get_feature_vector(tweet):
        uni_feature_vector = []
        bi_feature_vector = []
        words = tweet.split()
        for i in range(len(words) - 1):
            word = words[i]
            next_word = words[i + 1]
            if unigrams.get(word):
                uni_feature_vector.append(word)
            if USE_BIGRAMS:
                if bigrams.get((word, next_word)):
                    bi_feature_vector.append((word, next_word))
        if len(words) >= 1:
            if unigrams.get(words[-1]):
                uni_feature_vector.append(words[-1])
        return uni_feature_vector, bi_feature_vector
    
    def extract_features_t(tweets, batch_size=1, test_file=True, feat_type='presence'):
        num_batches = int(np.ceil(len(tweets) / float(batch_size)))
        for i in range(num_batches):
            batch = tweets[i * batch_size: (i + 1) * batch_size]
            features = lil_matrix((batch_size, VOCAB_SIZE))
            labels = np.zeros(batch_size)
            for j, tweet in enumerate(batch):
                if test_file:
                    tweet_words = tweet[1][0]
                    tweet_bigrams = tweet[1][1]
                
                if feat_type == 'presence':
                    tweet_words = set(tweet_words)
                    tweet_bigrams = set(tweet_bigrams)
                for word in tweet_words:
                    idx = unigrams.get(word)
                    if idx:
                        features[j, idx] += 1
                if USE_BIGRAMS:
                    for bigram in tweet_bigrams:
                        idx = bigrams.get(bigram)
                        if idx:
                            features[j, UNIGRAM_SIZE + idx] += 1
           
           
            yield features
    
    
    
    
    def process_tweets(line, test_file=True):
        tweets=[] 
        tweet_id, tweet = line.split('~`')           
        feature_vector = get_feature_vector(tweet)            
        tweets.append((tweet_id, feature_vector))
        return tweets
    
    ###########################################################################
    ###########################################################################
    line= "134~`"+tweet
    tweet_id, tweet = line.split('~`')   
    tweet=s.preprocess(tweet)
    print(tweet)
    
    test_tweets = process_tweets(line, test_file=True)
    for test_set_X in extract_features_t(test_tweets, test_file=True, feat_type=FEAT_TYPE):
        
        if FEAT_TYPE == 'frequency':
            
            test_set_X = tfidf.transform(test_set_X)
    
#    if(clf.predict(test_set_X) or clf1.predict(test_set_X)==1):
#        print("\nHappy or Mental state OK")
#    else:
#        print("\nMental state not OK")
#    print(clf.predict(test_set_X))
#    print(clf1.predict(test_set_X))
    #print(eclf.predict(test_set_X))
    x,y = clf.predict(test_set_X),clf1.predict(test_set_X)
    #print(int((x or y)[0]))
    return int((x or y)[0])

# tw = "i miss you guys too i think im wearing skinny jeans a cute sweater and heels not really sure what are you doing today"    
# predict(tw)
