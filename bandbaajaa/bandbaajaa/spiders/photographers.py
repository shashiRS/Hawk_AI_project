# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import pdb
import re

class PhotographersSpider(scrapy.Spider):
    name = "photographers"
    allowed_domains = ["bandbaajaa.com"]
    start_urls=['http://www.bandbaajaa.com/bangalore/photographers']
    
    def parse(self,response):
        url=[]
        for i in response.css('div.item-info >div >div'):
        	print(i.css('a ::attr(href)').extract())
        	# url.append(i.css('a ::attr(href)').extract())

        for link in url:
      
            yield SplashRequest(link, self.parseurl,endpoint='render.json')

    def parseurl(self,response):
    	print(response.url)