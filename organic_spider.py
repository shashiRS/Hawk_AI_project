# -*- coding: utf-8 -*-
import scrapy
import pdb
from six.moves import xmlrpc_client as xmlrpclib 
import csv
import pdb
import base64
from datetime import datetime, timedelta, date
from urllib import urlopen 
import urllib
import requests



username="admin"
password="123456"
dbname="Halk_AI_20170927"
url='http://192.168.0.120:9000'
proxy = xmlrpclib.ServerProxy("http://192.168.0.120:9000")

item2=[]
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url),allow_none=True)
common.version()
uid = common.authenticate(dbname, username, password, {})


models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url),allow_none=True)
key=models.execute_kw(dbname, uid, password,
                    'keyword.prject_wise_grid', 'search',[[['name', '=','Default'],['project_id','=',13]]])

            
key1=models.execute_kw(dbname, uid, password,
            'keyword.prject_wise_grid', 'read',
            [key], {'fields': ['id','name']})

temp_id = models.execute_kw(dbname, uid, password, 'cw.test.module', 'create', [{
                'name':13,
                'stage_id':key1[0]['id']
                
                
                }])

class HalkSpider(scrapy.Spider):
    name = "halk"
    allowed_domains = ["google.co.in"]
    term=raw_input("Enter the project name: ")
    print("URL:"+urllib.quote(term))
    start_urls = ['http://www.google.co.in/search?q='+urllib.quote(term)]

    def parse(self, response):
        item_val={}
        name=''
        link=''
        for items in  response.css('h3.r > a   ::text').extract():
            name+=items
        for links in response.css('cite::text').extract():
            link+=links
                        
        target_url=response.urljoin(response.css("h3.r > a::attr(href)").extract_first())

        items_val={'name':name,
        'dis_link':link,
        'description':response.css(".st  ::text").extract_first(),
        'target_url':target_url}
        link_next=response.css('a.fl::attr(href)').extract()

        if item_val:
                check_id=models.execute_kw(dbname, uid, password,
                        'cw.organic_search_table_master', 'search_count',
                        [[['ad_name','=',item_val['name'] ],['orgnaic_main_id','=',temp_id],['stage_id','=',key1[0]['id']]]])
                if check_id==0:
                    temp_id2 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table_master', 'create', [{
                                'name':items_val['name'],
                                'website':items_val['target_url'],
                                'ad_name':items_val['name'],
                                'ad_desc':items_val['description'] ,
                                'adlink':items_val['dis_link'] ,
                                'stage_id':key1[0]['id'],
                                'orgnaic_main_id':temp_id,
                                
                                
                                }])
                    
                    
                    temp_id3 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table', 'create', [{
                                'name':items_val['name'],
                                'website':items_val['target_url'],
                                'ad_name':items_val['name'],
                                'ad_desc':items_val['description'] ,
                                'adlink':items_val['dis_link'] ,
                                'stage_id':key1[0]['id'],
                                'orgnaic_main_id':temp_id,
                                
                                
                                }])    
        for i in range(1,5):
            url=link_next[i]
            url=response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.parse_details,meta={'items': items_val})

    def parse_details(self,response):
      item_val = response.meta.get('items')
      item={}
      for items in  response.css('h3.r > a   ::text').extract():
            name+=items
        for links in response.css('cite::text').extract():
            link+=links
                        
        target_url=response.urljoin(response.css("h3.r > a::attr(href)").extract_first())

        items_val={'name':name,
        'dis_link':link,
        'description':response.css(".st  ::text").extract_first(),
        'target_url':target_url}
        link_next=response.css('a.fl::attr(href)').extract()

        if item_val:
                check_id=models.execute_kw(dbname, uid, password,
                        'cw.organic_search_table_master', 'search_count',
                        [[['ad_name','=',item_val['name'] ],['orgnaic_main_id','=',temp_id],['stage_id','=',key1[0]['id']]]])
                if check_id==0:
                    temp_id2 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table_master', 'create', [{
                                'name':items_val['name'],
                                'website':items_val['target_url'],
                                'ad_name':items_val['name'],
                                'ad_desc':items_val['description'] ,
                                'adlink':items_val['dis_link'] ,
                                'stage_id':key1[0]['id'],
                                'orgnaic_main_id':temp_id,
                                
                                
                                }])
                    
                    
                    temp_id3 = models.execute_kw(dbname, uid, password, 'cw.organic_search_table', 'create', [{
                                'name':items_val['name'],
                                'website':items_val['target_url'],
                                'ad_name':items_val['name'],
                                'ad_desc':items_val['description'] ,
                                'adlink':items_val['dis_link'] ,
                                'stage_id':key1[0]['id'],
                                'orgnaic_main_id':temp_id,
                                
                                
                                }])    
      yield item_val
       