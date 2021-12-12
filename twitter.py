# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:47:24 2019

@author: hp
"""

#####################################################################
#Twitter
def proceed(t_id):
    import tweepy 
    #from ibmWatson import ibms
    from model import predict
    #from grphy import gplot
    # Fill the X's with the credentials obtained by  
    # following the above mentioned procedure. 
    consumer_key = "AK2gnrwBqTsPzaZV4WpoDVMo4" 
    consumer_secret = "5kNUx2iU2ZCbkH8aZafL5uE3OFTEBvPhrRLOega9llUgkzlTeF"
    access_key = "1080507728588529664-3dIcQ9NI8cG8VwZHmLWhF1BGIYuxw7"
    access_secret = "hTrrGr36FgfRQHidFUFMHiEIfMUTxMAExXoBmmi7ZQ1OQ"
      
    # extract tweets 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    tweet_count = 20

    stuff = api.user_timeline(screen_name = t_id, include_rts=True, count = tweet_count, tweet_mode='extended')

    toa = []    #tweet to analyze

    for status in stuff:
        toa.append(status.full_text)
        
    #print(toa)

    ########################################################################
    #IBM
#     emotion = []
#     for i in range(tweet_count):
#         emotion.append(ibms(toa[i]))

#     #emotion = ['anger','sadness','joy','analytical','neutral','anger','sadness','joy']    
# #a = proceed('thevirdas')
#     #conversion to integer
#     em_int = []
#     for i in range(tweet_count):      
#         if emotion[i] in ['neutral','tentative']:
#             em_int.append(0)
#         elif emotion[i] in ['analytical','confident']:
#             em_int.append(1)
#         elif emotion[i] == 'joy':
#             em_int.append(3)
#         elif emotion[i] == 'anger':
#             em_int.append(-1)
#         elif emotion[i] == 'worry':
#             em_int.append(-2)
#         elif emotion[i] == 'sadness':
#             em_int.append(-3)
            
    ########################################################################
    ########################################################################
    #model
    em_int = []
    for i in range(tweet_count):
        em_int.append(predict(toa[i]))

    emotion = []
    for i in range(tweet_count):
        if em_int[i] == 0:
            emotion.append("Negative")
        else:
            emotion.append("Positive")
    ########################################################################
    #graph plot
    #gplot(em_int)

    #return dict(zip(toa,emotion))
    toSend = []
    for i,j,k in zip(toa,emotion,em_int):
	    toSend.append({"t":i,"r":j,"c":k})
    return toSend