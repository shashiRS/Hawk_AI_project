# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import pdb
import time
import json
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.http import FormRequest
from collections import OrderedDict
import pandas

class IndiapropertydataPySpider(scrapy.Spider):
    name = "indiapropertydata.py"
    allowed_domains = ["indiaproperty.com"]
    def __init__(self, *args, **kwargs):
        self.start_url=[]
        url='https://www.indiaproperty.com/searchs/ci=bangalore&pt=allresidential&litype=sale&frm=&srchtype=&f=srch&withapi=0&view=list&nlpsearch=1?q=yelahanka&pageno=3&sof=51'
        self.start_url.append(url)
               
           
        super(IndiapropertydataPySpider, self).__init__(*args, **kwargs)
    def start_requests(self):
        for url in self.start_url:
            yield SplashRequest(url, callback=self.parse)

    def parse(self, response):
        
        # response.css('div.col-xs-4 >div.new-search-grid-box-gridtop >a ::attr(href)').extract()
        print(len(response.css('div.pg_search >div.pagination >a').extract()))
        pdb.set_trace()

