# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class SimageSpider(scrapy.Spider):
    name = "simage"
    allowed_domains = ["google.co.in"]
    def __init__(self, *args, **kwargs):
        self.start_url=[]
        url='https://www.google.co.in/search?q=prestige+jindal+city&source=lnms&tbm=isch'
        self.start_url.append(url)
        super(SimageSpider, self).__init__(*args, **kwargs)
    
    def start_requests(self):
        for url in self.start_url:
            yield SplashRequest(url, callback=self.parse)
    def parse(self, response):
        print(response.body)
