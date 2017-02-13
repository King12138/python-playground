# -*- coding: utf-8 -*-

'''
Created on 2017-02-11 16:07:41
提取Twitter数据实体
@author: zhoujiagen
'''
# 字段的说明:
# https://dev.twitter.com/overview/api/tweets
# https://dev.twitter.com/overview/api/entities
# https://dev.twitter.com/overview/api/users

from nltk.corpus import twitter_samples
# from nltk.twitter.common import json2csv
import json

input_file = twitter_samples.abspath("tweets.20150430-223406.json")

# 准备数据
#
# 图数据模型
# 节点: User, Word, URL, Hashtag
# 关系: mentions_user, retweets_user, follows_user, mentions_hashtag, uses_word, mentions_url
# user.screen_name(user), user.name, user.location
# text
# entities.hashtags
# entities.user_mentions(mentions)
# entities.urls
# retweeted
def extract_tweet_info(tweet):
    result = {}

    user = tweet[u'user']
    result['user'] = _format(user[u'screen_name'].encode('utf8'))
    result['name'] = _format(user[u'name'].encode('utf8'))
    result['location'] = _format(user[u'location'].encode('utf8'))
    result['text'] = _format(tweet[u'text'].encode('utf8'))

    entities = tweet[u'entities']
    hashtags = entities[u'hashtags']
    user_mentions = entities[u'user_mentions']
    urls = entities[u'urls']

    result['hashtags'] = [_format(hashtag[u'text'].encode('utf8')) for hashtag in hashtags]
    result['mentions'] = [_format(um[u'screen_name'].encode('utf8')) for um in user_mentions]
    result['urls'] = [_format(url[u'expanded_url'].encode('utf8')) for url in urls]

    retweeted = tweet[u'retweeted']
    if retweeted:
        result['retweetuser'] = {'user': result['user'], 'name': result['name'], 'location': result['location']}

    return result

def _format(string):
    return string.replace('\'', '_').replace('"','')

with open(input_file) as fp:
#     json2csv(fp, 'extracted_tweets.txt',
#         ['user.screen_name', 'user.name', 'user.location', 'text', 'retweeted',
#         'entities.hashtags'
#         ])

#     json2csv_entities(fp, 'tweets.20150430-223406.hashtags.csv',
#         ['id', 'text'], 'hashtags', ['text'])

    f = open('extracted_tweets.txt', 'w')
    for line in fp:
        tweet = json.loads(line)
        # print extract_tweet_info(tweet)
        f.write(str(extract_tweet_info(tweet)) + '\n')
        #break # for debug
    f.close()
