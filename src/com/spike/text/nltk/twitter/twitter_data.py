# -*- coding: utf-8 -*-

'''
Created on 2017-02-11 15:36:04
Twitter数据
@author: zhoujiagen
'''

# from nltk.twitter import Twitter
# tw = Twitter()

from nltk.corpus import twitter_samples
from pprint import pprint

# 文件ID
fileids = twitter_samples.fileids()
print fileids

print

# 查看文件内容
# 字段的说明: https://dev.twitter.com/overview/api/tweets
docs = twitter_samples.docs('tweets.20150430-223406.json')
for doc in docs[:1]:
    pprint(doc)
    print

print

# 查看文件中text字段
strings = twitter_samples.strings('tweets.20150430-223406.json')
for string in strings[:10]:
    print(string)

print 



