# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import pdb



class DjSpider(scrapy.Spider):
    name = "dj"
    allowed_domains = ["weddingz.in"]
    start_urls=['https://weddingz.in/dj/bangalore/']

    def parse(self, response):
        url=[]
        for i in response.css('div.vendor-card >div.image'):
            url.append("https://weddingz.in/"+i.css('a:nth-child(1) ::attr(href)')[0].extract())
        # print url
        for link in url:
      
            yield SplashRequest(link, self.parseurl,endpoint='render.json')

    def parseurl(self,response):
        item={
            'photoghraphy_title':response.css('div.venue-card__title >div.text-content ::text').extract(),
            'photoghraphy_description':response.css('div.about-summary >div.summary >div.tab-data::text').extract(),
            'photoghraphy_address':response.css('div.overview-col >div.address ::text').extract(),
            'photoghraphy_number':response.css('div.overview-col >a.number ::attr(href)').extract() ,
            'photoghraphy_photos':response.css('div.venue-card >div >div >div >div.main-img >img ::attr(data-src)').extract(),
            }
        yield item
