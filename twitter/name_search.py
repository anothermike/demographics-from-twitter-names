# -*- coding: utf-8 -*-
import csv

class NameSearch(object):

    def __init__(self):
      self.names = []
      with open('../spider/names_with_year_prob.csv', 'rb') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        for row in file:
          o = {}
          o['name'] = row[0]
          o['sex'] = row[2]

          try:
            o['prob'] = float(row[1])
            o['year'] = int(row[3])
          except ValueError, e:
            print "An error has occured: " + str(e)
            print ValueError
          
          self.names.append(o)
      
    def search(self, name):
      res = []
      for e in self.names:
        if name in e['name'].decode('utf8'):
          res.append(e)
      return sorted(res, key=lambda k: k.get('prob', 0))     