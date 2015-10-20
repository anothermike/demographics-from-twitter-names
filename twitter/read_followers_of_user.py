# -*- coding: utf-8 -*-
import config
import tweepy
from name_search import NameSearch

class TwitterFollowers(NameSearch):

    def __init__(self, con_secret, con_secret_key, token_key, token):      
      super(TwitterFollowers, self).__init__()
      self.con_secret = con_secret
      self.con_secret_key = con_secret_key
      self.token_key = token_key
      self.token = token
      
      auth = tweepy.OAuthHandler(self.con_secret, self.con_secret_key)
      auth.set_access_token(self.token, self.token_key)

      self.t = tweepy.API(auth)
    
    def get_followers(self, screen_name):
      followers = []
      i = 0
      # if you increase the number of returned results, you will probably have to deal with rate limits from Twitter
      for user in tweepy.Cursor(self.t.followers, screen_name=screen_name, count=200).items():
        followers.append(user.name.split(" ")[0])
        i = i + 1
        if (i > 200):
          break
          
      return followers

twitter_name = 'sevenval'
tn = TwitterFollowers(config.con_secret, config.con_secret_key, config.token_key, config.token)
follower_names = tn.get_followers(twitter_name)
r = []
for forename in follower_names:
  o = tn.search(forename)
  if o:
    r.append(o[-1]) #get the name with highest probability

f = open('demographics_' + twitter_name + '.csv','w')
f.write('name;sex;age\n')
for o in r:
  f.write(o['name'] + ';' + o['sex'] +';' + str( 2015 - o['year']) + '\n')
f.close()