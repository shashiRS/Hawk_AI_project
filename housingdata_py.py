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
from scrapy.http.request import Request


class HousingdataPySpider(scrapy.Spider):
    name = "housingdata.py"
    allowed_domains = ["housing.com"]
    start_urls =['https://housing.com/in/buy/search?f=eyJiYXNlIjpbeyJ0eXBlIjoiUE9MWSIsInV1aWQiOiJjZDNiNzE4MzA1MDdlMTM2NDkxMCIsImxhYmVsIjoiWWVsYWhhbmthIn1dLCJub25CYXNlQ291bnQiOjAsInYiOjIsInMiOiJkIn0%3D']

    def parse(self, response):
    	print(response.css('div.lst-dtls.inline-blk >div>a.lst-title ::text').extract())
    	for i in response.css('div.lst-dtls.inline-blk >div>a.lst-title ::attr(href)'):
    		url="https://housing.com/"+i.extract()
    		yield Request(url,self.parse_detail)
    def parse_detail(self,response):
    	# pdb.set_trace()
        # data=response.body
        Price_trend=''
        Builder=''
        urls=[]
        data=response.xpath("//script").extract()
        for i in data:
            try:
                Price_trend=i.split("init_options =")[1].split('price_trends')[1].split("avg_price_per_sqft")[0].split("[")[1].split("],")[0]
            except:
                pass
        rera=''
        try:
            rera=response.css('div.entity.rera-entity >span >span.value ::text')[1].extract()
            Builder=response.css('div.mt-10.txt.uc.builder-text ::text')[2].extract()
            for i in response.css('div.bordered-card.card >div.apf-slider-container.show-scroll >div.apf-slider-wrapper >a >div.bank-image ::attr(style)').extract():
                dada=i.split("url('")[1]
                ul=dada.split("')")[0]
                urls.append(ul)

        except:
            pass
    	item={
    	'Locality':response.css('div.location-info.grey.txt.mt-10 ::text').extract(),
    	'Base_price':response.css('span.price ::text').extract(),
    	'Price_per_sqft':response.css('div.info-value::text')[0].extract(),
    	'Apartments':response.css('div.info-value::text')[1].extract(),
    	'PossessionDate':response.css('div.info-value >span ::text').extract(),
    	'Sizes_pricerange':response.css('div.info-value::text')[4].extract(),
    	'RERA-ID':rera,
        'offer':response.css('div#offers-container ::text').extract(),
        'Pricetrend_values':Price_trend,
        'About_builder_desc':response.css('div.builder-desc ::text').extract(),
        'Insights_into_neighbourhood':response.css('div.locality-desc ::text').extract(),
        'Amenities':response.css('div.project-desc >ul.desc-para.project-higlights ::text').extract(),
        'About_project':response.css('div.project-desc >p.desc-para ::text').extract(),
        'Builder_by':Builder,
        'Homeloan':urls,
    	}
        yield item

        
