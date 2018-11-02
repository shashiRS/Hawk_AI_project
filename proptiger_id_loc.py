# -*- coding: utf-8 -*-
import scrapy


class ProptigerIdLocSpider(scrapy.Spider):
    name = 'proptiger_id_loc'
    allowed_domains = ['proptiger.com']
    start_urls = ['https://www.proptiger.com/bangalore/all-localities']

    def parse(self, response):
        id_loc=''
        name_loc=''
        for x in response.css('div.locality-details >ul >li >a'):
            temp=x.css('a::attr(href)').extract_first()
            id_loc=temp.split('overview-')[1]
            name_loc=x.css('a::text').extract_first()
            item={'id_loc':id_loc,
                  'name_loc':name_loc}
            yield item
        
        link_list=response.css('div.container ul.custom-pagi >li >a.no-ajaxy::attr(href)').extract()
        for i in range(1,len(link_list)):
            link=response.urljoin(link_list[i])
            yield scrapy.Request(link, callback=self.parse)