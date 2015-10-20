# -*- coding: utf-8 -*-
import config
from twitter import *
from name_search import NameSearch

class TwitterNotifications(NameSearch):

    def __init__(self, con_secret, con_secret_key, token_key, token):
      super(TwitterNotifications, self).__init__()
      
      self.con_secret = con_secret
      self.con_secret_key = con_secret_key
      self.token_key = token_key
      self.token = token
      
      self.t = Twitter(auth=OAuth(self.token, self.token_key, self.con_secret, self.con_secret_key))
      
    def get_twitter_names(self):
      data = self.t.statuses.mentions_timeline(count=10)
      for reply in data:
        n = reply['user']['name'].split(" ")[0]
        print n
        r = self.search(n)
        if r:
          print r[-1]
        
tn = TwitterNotifications(config.con_secret, config.con_secret_key, config.token_key, config.token)
tn.get_twitter_names()

