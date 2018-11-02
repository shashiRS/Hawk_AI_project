# -*- coding: utf-8 -*-
import scrapy


class PincodeAreaSpider(scrapy.Spider):
    name = 'pincode_area'
    allowed_domains = ['mapsofindia.com']
    start_urls = ['https://www.mapsofindia.com/pincode/india/karnataka/bangalore/']

    def parse(self, response):
        for x in response.css('table.extrtable >tr'):
            pincode=''
            area_name=''
            pincode=x.css('td >b ::text').extract_first()
            area_name=x.css('td >a ::text').extract_first()
            item={'pincode':pincode,
                  'area_name':area_name}
            yield item
