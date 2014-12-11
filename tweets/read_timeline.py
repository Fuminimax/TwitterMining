# -*- coding: utf-8 -*-

import MeCab
import tweepy
import json
import sys
import re
import csv
from pprint import pprint
from requests_oauthlib import OAuth1Session
from urlparse import ParseResult

CK = 'QFOiO0R9A1oqK94UnjI3Q'
CS = '9lC3I6cBBNK4TLo6vZFHKpcunJs1FZVGxMAOow8ucs'
AT = '16167279-9NU9kRgh7Len6teTRax78vlxa3lQc3urgNkzsa8PC'
AS = '4QitfT0CoQVMynWyQdC7UMyYWynMheMxMNF6PPD48'

#tw = OAuth1Session(CK, CS, AT, AS)
#url = 'https://stream.twitter.com/1.1/statuses/sample.json'
#params = {}

#tweets = tw.get(url, params = params)
#print tweets.status_code
#timeline = json.loads(tweets.text)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if sys.argv[1].decode('utf-8') in status.text:
            print (status.user.screen_name+' : '+status.text.encode('utf-8'))
            
    def on_data(self, data):
        #print data
        txt = json.loads(data, "utf-8")
        dst = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', txt["text"]) 
        dst = re.sub(r'(?:^|[^ｦ-ﾟー゛゜々ヾヽぁ-ヶ一-龠ａ-ｚＡ-Ｚ０-９a-zA-Z0-9&_\/]+)#([ｦ-ﾟー゛゜々ヾヽぁ-ヶ一-龠ａ-ｚＡ-Ｚ０-９a-zA-Z0-9_]*[ｦ-ﾟー゛゜々ヾヽぁ-ヶ一-龠ａ-ｚＡ-Ｚ０-９a-zA-Z]+[ｦ-ﾟー゛゜々ヾヽぁ-ヶ一-龠ａ-ｚＡ-Ｚ０-９a-zA-Z0-9_]*)', '', dst)
        dst = re.sub(r'@[^\s]+', '', dst)
        print dst
        mc = MeCab.Tagger("-Ochasen")
        en_dst = dst.encode('utf-8')
        parseResult = mc.parseToNode(en_dst)
        while parseResult:
            pos = parseResult.feature.split(',')
            if pos[0] != 'BOS/EOS' or parseResult.surface != '' or parseResult.surface != 'RT':
                if pos[0] == '名詞' and len(unicode(parseResult.surface, 'utf-8')) > 1 :
                    print parseResult.surface + ',' + parseResult.feature
            parseResult = parseResult.next
            #words = csv.reader(rows, delimiter='\t')
            #print words[3]
        #wordOfPart = words[3]
        #pprint(parseResult)
        #print txt["text"]
        return True
   
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

stream_listener= tweepy.Stream(auth, CustomStreamListener())
timelines = stream_listener.sample(languages=['ja'])
#timelines = stream_listener.filter(languages=['ja'])

#print timelines
#for tweet in timelines:
#    txt = json.loads(tweet, "utf-8")
#    print txt["id"].decode
    
