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

class PropertywaladataPySpider(scrapy.Spider):
    name = "propertywaladata.py"
    allowed_domains = ["propertywala.com"]
    def __init__(self, *args, **kwargs):
        self.start_url=[]
        for i in range(1,25):
	        url='https://www.propertywala.com/projects/type-residential_apartment_flat/location-bangalore_karnataka?page='+i
	        self.start_url.append(url)
               
           
        super(MakaandataPySpider, self).__init__(*args, **kwargs)
    def start_requests(self):
        for url in self.start_url:
            yield SplashRequest(url, callback=self.parse)

    def parse(self, response):
        pdb.set_trace()
        list1=response.css('a.projName ::attr(href)').extract()
        for i in list1:
        	yield SplashRequest(url, callback=self.parse_details)

        
    def parse_details(self):
    	pdb.set_trace()
    	