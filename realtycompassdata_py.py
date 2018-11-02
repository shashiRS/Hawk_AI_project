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


class RealtycompassdataPySpider(scrapy.Spider):
    name = "realtycompassdata.py"
    allowed_domains = ["realtycompass.com"]
    # start_urls =['https://www.realtycompass.com/search-realtycompass.php?q=Yelahanka%20bangalore']
    def __init__(self, *args, **kwargs):
        self.start_url=[]
        url='https://www.realtycompass.com/search-realtycompass.php?q=Yelahanka%20bangalore'
        self.start_url.append(url)
               
           
        super(RealtycompassdataPySpider, self).__init__(*args, **kwargs)
    def start_requests(self):
        for url in self.start_url:
            yield SplashRequest(url, callback=self.parse)

    def parse(self, response):
        pdb.set_trace()
        
