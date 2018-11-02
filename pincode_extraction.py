# -*- coding: utf-8 -*-
import scrapy


class PincodeExtractionSpider(scrapy.Spider):
    name = 'pincode_extraction'
    allowed_domains = ['pin-code.net.in']
    start_urls = ['http://www.pin-code.net.in/karnataka/bangalore']

    def parse(self, response):
        url_list=response.css('table >td >h2 >a::attr(href)').extract()
        self.final_url=[]
        for item in url_list:
            url=response.urljoin(item)
            yield scrapy.Request(url,callback=self.fetch_detail)
            
            
    def fetch_detail(self, response):
        url_target=response.css('table >td >h2 >a::attr(href)').extract()
        self.final_url.append(x for x in url_target)
        
        for item in url_target:
            url=response.urljoin(item)
            yield scrapy.Request(url,callback=self.fetch_detail1)
        
        
    def fetch_detail1(self, response):
        final_dict={}
        for x in response.css('table.mtable >tbody >tr.tcw '):
            key=''
            value=''
            z={}
            for x1 in x.css('td')[0].css('td ::text').extract():
                key+=x1
            for x1 in x.css('td')[1].css('td ::text').extract():
                value+=x1
            z={key.strip():value.strip()}
            
            final_dict.update(z)    
        
        yield final_dict
             