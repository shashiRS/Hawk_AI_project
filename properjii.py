# -*- coding: utf-8 -*-
import scrapy

class PopulationItem(scrapy.Item):
    head = scrapy.Field()
    data = scrapy.Field()
# term=raw_input("Search by project name: ")
class ProperjiiSpider(scrapy.Spider):
    name = 'properjii'
    allowed_domains = ['properji.com']
    
    # start_urls = ['http://properji.com/analysis/'+term]

    def parse(self, response):
        # print(response.body)
       
        tabl=response.css('div.col-md-6 >div.box-success >div.box-body >div.table-responsive >table.table-striped >tbody')
        print tabl
        it=[]
        items={}
        for row in tabl:
            item = PopulationItem()
            item['head'] = row.css('tr >th ::text').extract()
            item['data'] = row.css('tr >td ::text').extract()
            # print item['data'][0]
            # print item['data'][1]
            # print item['data'][2]
            # print(len(item['data']))
            # for row in zip((value) for value in item.items()):
            #     print(row)
        items={
        'amenities':response.css('div#projectdescription >ul >li:nth-child(3) ::text').extract(),
        'demand':response.css('div#projectdescription >ul >li:nth-child(2) ::text').extract(),
        'approved':response.css('div#projectdescription >ul >li:nth-child(1) ::text').extract(),
        'proj_description':response.css('div#projectdescription >p::text').extract(),
        }
        itemss={}
        for i in response.css('div.clearfix >div >div >div >div.box-body >div.clearfix'):
            headder=''
            values=''
            hed=i.css('div.col-xs-4::text').extract()
            valu=i.css('div.col-xs-8::text').extract()
            for h in hed:
                headder=h
            for h in valu:
                values=h
            itemss={
            headder:values
               }
            items.update(itemss)
            
                
         
        yield items


