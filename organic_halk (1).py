# -*- coding: utf-8 -*-
import scrapy
import pdb
from six.moves import xmlrpc_client as xmlrpclib 
import csv
import pdb
import base64
from datetime import datetime, timedelta, date
import urllib
import urllib.parse
import requests
from scrapy.crawler import CrawlerProcess



username="admin"
password="123456"
dbname="Halk_AI_20170927"
url='http://localhost:9002'
proxy = xmlrpclib.ServerProxy("http://localhost:9002")

item2=[]
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url),allow_none=True)
common.version()
uid = common.authenticate(dbname, username, password, {})


models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url),allow_none=True)



class OrganicHalkSpider(scrapy.Spider):
    name = 'organic_halk'
    allowed_domains = ['google.co.in']
    
    
    def __init__(self, name=None,proj_id=None,scrape_id=None,stage_id=None, *args, **kwargs):

        self.start_urls = ['http://www.google.co.in/search?q=%s'%(urllib.parse.quote(name))]
        key=models.execute_kw(dbname, uid, password,
                    'keyword.prject_wise_grid', 'search',[[['id', '=',stage_id],['project_id','=',int(proj_id)]]])

            
        self.key1=models.execute_kw(dbname, uid, password,
            'keyword.prject_wise_grid', 'read',
            [key], {'fields': ['id','name']})
        
        self.scrape_id=scrape_id
        self.proj_id=proj_id
        self.stage_id=stage_id
        super(OrganicHalkSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for q1 in response.css('div.g'):
            items_val={}
            name=''
            link=''
            domain=''
            description=''
            print (q1.css('cite ::text').extract())
            if q1.css('cite ::text').extract():
                for items in q1.css("h3.r > a ::text ").extract():
                    name+=items
                for links in q1.css('cite ::text').extract():
                    link+=links
                print(link)  
                
                dommm=link.split('/')[2]
                print(dommm)
            
                domn=''                        
                if 'www' in dommm:
                    domn=dommm.split('www.',1)[1]

                else:
                    domn=dommm
                print(domn)
                if q1.css("span.st ::text").extract():
                    for dec in q1.css("span.st ::text").extract():
                        description+=dec
                
                target_url=response.urljoin(q1.css("h3.r > a::attr(href)").extract_first())

                items_val={'name':name,
                    'dis_link':link,
                    'description':description,
                    'target_url':target_url,
                    'domain':link
                    }
                
                if items_val:
                    
                    check_id=models.execute_kw(dbname, uid, password,
                            'cw.organic_search_table_master', 'search_count',
                            [[['name','=',items_val['name']],['orgnaic_main_id','=',int(self.scrape_id)],['stage_id','=',self.key1[0]['id']]]])
                    if check_id==0:
                        temp_id2 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table_master', 'create', [{
                                    'name':items_val['name'],
                                    'website':items_val['target_url'],
                                    'ad_name':items_val['description'],
                                    'web_domain':items_val['domain'] ,
                                    'stage_id':self.key1[0]['id'],
                                    'orgnaic_main_id':int(self.scrape_id),
                                    
                                    
                                    }])
                        
                        
                        #temp_id3 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table', 'create', [{
                                    #'name':items_val['name'],
                                    #'website':items_val['target_url'],
                                    #'ad_name':items_val['description'],
                                    #'web_domain':items_val['domain'] ,
                                    #'stage_id':self.key1[0]['id'],
                                    #'orgnaic_main_id':int(self.scrape_id),
                                    
                                    
                                    #}])   
        link_next=response.css('a.fl::attr(href)').extract()                
        for i in range(1,5):
            url=link_next[i]
            url=response.urljoin(url)
            #yield scrapy.Request(url=url,callback=self.parse_details,meta={'items': items_val})
            yield scrapy.Request(url=url,callback=self.parse_details,meta={'items': items_val})



    def parse_details(self,response):
        #items_val = response.meta.get('items')
        item={}
        for q1 in response.css('div.g'):
            item_val={}
            name=''
            link=''
            domain=''
            description=''
            if q1.css('cite ::text').extract():
                for items in q1.css("h3.r > a ::text ").extract():
                    name+=items
                for links in q1.css('cite ::text').extract():
                    link+=links
                print(link)    
                #dommm=link.split('/')[2]
                #print(dommm)
            
                #domn=''                        
                #if 'www' in dommm:
                    #domn=dommm.split('www.',1)[1]

                #else:
                    #domn=dommm
                if q1.css("span.st ::text").extract():
                    for dec in q1.css("span.st ::text").extract():
                        description+=dec
                
                target_url=response.urljoin(q1.css("h3.r > a::attr(href)").extract_first())

                item_val={'name':name,
                    'dis_link':link,
                    'description':description,
                    'target_url':target_url,
                    'domain':link
                    }
                
                if item_val:
                    
                    check_id=models.execute_kw(dbname, uid, password,
                            'cw.organic_search_table_master', 'search_count',
                            [[['name','=',item_val['name']],['orgnaic_main_id','=',int(self.scrape_id)],['stage_id','=',self.key1[0]['id']]]])
                    if check_id==0:
                        temp_id2 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table_master', 'create', [{
                                    'name':item_val['name'],
                                    'website':item_val['target_url'],
                                    'ad_name':item_val['description'],
                                    'web_domain':item_val['domain'] ,
                                    'stage_id':self.key1[0]['id'],
                                    'orgnaic_main_id':int(self.scrape_id),
                                    
                                    
                                    }])
                        
                        
                        #temp_id3 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table', 'create', [{
                                    #'name':item_val['name'],
                                    #'website':item_val['target_url'],
                                    #'ad_name':item_val['description'],
                                    #'web_domain':item_val['domain'] ,
                                    #'stage_id':self.key1[0]['id'],
                                    #'orgnaic_main_id':int(self.scrape_id),
                                    
                                    #}])
                
        yield item_val
        