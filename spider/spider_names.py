# -*- coding: utf-8 -*-

import scrapy
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
        
    start_urls = ["http://www.beliebte-vornamen.de/jahrgang/j" + str(i) for i in range(1890, 2015)]
    global years_with_names
    years_with_names = {}

    def __init__(self):
      dispatcher.connect(self.spider_closed, signals.spider_closed)
    
    def getNameDict(self, name, pos, sex, year):
      o = {}
      o['sex'] = sex
      o['name'] = name
      prob = 1
      if pos <= 10:
        prob = 1.5 + (10 - pos) * 0.1 ##2,5% bis 1,5% top 10... danach 1% pro eintrag
        
      if year <= 1980:
        prob = prob * (year - 1889) 
      else:
        prob = prob * (2015 - year)
        
      o['prob'] = prob
      return o
      
    def parse(self, response):
      year = response.url.split("/")[-1][-4:]

      names = []

      i = 0
      for h in response.xpath('//ol[1]/li/a/text()').extract():
        o = self.getNameDict(h, i, 'female', int(year))
        names.append(o)
        i = i + 1
      
      i = 0
      for h in response.xpath('//ol[2]/li/a/text()').extract():
        o = self.getNameDict(h, i, 'male', int(year))
        names.append(o)
        i = i + 1

      years_with_names[year] = names
      
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        
    def spider_closed(self, spider):
      f = open('names_with_year_prob.csv.new','w')
      f.write('name;prob_fac;sex;year\n') # python will convert \n to os.linesep
      for year in years_with_names:
        for o in years_with_names[year]:
          f.write(o['name'].encode('utf8') + ';' + str(o['prob']) +';' + o['sex'] +';' + year + '\n') # python will convert \n to os.linesep
          print o['name']
          #f.write(o)
      
      f.close()