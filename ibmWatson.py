# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:15:46 2019

@author: hp
"""
#import json
def ibms(tweet):
    from watson_developer_cloud import ToneAnalyzerV3
    
    tone_analyzer = ToneAnalyzerV3(
            iam_apikey = 'cG_v7eEE9EPWA1KiFAknHeOpkK0s-pjv2QMAN6nGPQSX',
            version = '2017-09-21',
            url = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api'
            )
    
    #tweet = ''''''
    result = tone_analyzer.tone(tweet,content_type='text/plain').get_result()
    
    try:
        return(result['document_tone']['tones'][0]['tone_id'])
    except IndexError:
        return('neutral')

#ibms()