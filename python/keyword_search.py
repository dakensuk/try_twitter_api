#!/usr/bin/env python
# coding: utf-8

# In[25]:


import json,config
from requests_oauthlib import OAuth1Session

ck = config.consumer_key
cs = config.consumer_secret
at = config.access_token
ats = config.access_token_secret

twitter = OAuth1Session(ck, cs, at, ats) 

url = 'https://api.twitter.com/1.1/search/tweets.json'

print("Please input keyword")
tweet = input('>> ')
count=20
result_type='mixed'

params = {'q' : tweet, 'count': count, 'result_type': result_type}

res = twitter.get(url, params = params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    
    with open('result.txt', 'w') as f:
        for line in timelines['statuses']:
            if 'http' in line['text']:
                print(line['user']['name'] + ':' + line['text'], file=f)
                print(line['created_at'], file=f)
                print('---------------------------------------------------', file=f)

# output result
    with open('result.txt') as f:
        data1 = f.read() 

    print(type(data1))
    lines1 = data1.split('\n')
    for line in lines1:
        print(line)

else:

    print('Failed: %d' % res.status_code) 


# In[ ]:




