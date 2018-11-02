# -*- coding: utf-8 -*-
import scrapy


class CommonFloorAreaIdPySpider(scrapy.Spider):
    name = 'common_floor_area_id.py'
    allowed_domains = ['commonfloor.com']
    start_urls = ['https://www.commonfloor.com/Hyderabad-city']

    def parse(self, response):
        for items in response.css('div.localitysas li >div >a'):
            name=''
            id1=''
            name=items.css('a::text').extract()
            id1=items.css('a::attr(data-prop-locality-id)').extract()
            item={'name':name,'id':id1}
            yield item
