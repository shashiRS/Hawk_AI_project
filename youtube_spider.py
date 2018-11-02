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

# username="admin"
# password="123456"
# dbname="Halk_AI_20170927"
# url='http://192.168.0.120:9000'
# proxy = xmlrpclib.ServerProxy("http://192.168.0.120:9000")

# item2=[]
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url),allow_none=True)
# common.version()
# uid = common.authenticate(dbname, username, password, {})


# models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url),allow_none=True)
# key=models.execute_kw(dbname, uid, password,
#                     'keyword.prject_wise_grid', 'search',[[['name', '=','Default'],['project_id','=',13]]])

            
# key1=models.execute_kw(dbname, uid, password,
#             'keyword.prject_wise_grid', 'read',
#             [key], {'fields': ['id','name']})

# temp_id = models.execute_kw(dbname, uid, password, 'cw.test.module', 'create', [{
#                 'name':13,
#                 'stage_id':key1[0]['id']
                
                
#                 }])

class HalkSpider(scrapy.Spider):
    name = "spione"
    allowed_domains = ["google.co.in"]
    term=raw_input("Enter the project name: ")
    print("URL:"+urllib.quote(term))
    start_urls = ['https://www.youtube.com/results?search_query='+urllib.quote(term)]

    def parse(self, response):
        item_val={}
        name=''
        link=''
        linkq=[]
        view=''
        domain=[]
        names=[]
        # print(response.body)
        for items in  response.css('h3.yt-lockup-title > a::text').extract():
            name=items
            names.append(items)
        for links in response.css('h3.yt-lockup-title > a::attr(href)').extract():
            link="https://www.youtube.com"+links
            linkq.append(link)
        publish=[]   
        count=0
        for views in response.css('ul.yt-lockup-meta-info > li ::text').extract():
          count=count+1
          view=view+" "+views
          if count==2:
              publish.append(view)
              view=''
              count=0
        
        print(publish)
        print(linkq)
        print(names)   

        pdb.set_trace()

        target_url=response.urljoin(response.css('h3.yt-lockup-title > a::attr(href)').extract_first())
        for linkw in response.css('h3.yt-lockup-title > a::attr(href)').extract():
          dommm=linkw.split('/',1)[0]
          print(dommm)
              
          domn=''                        
          if 'www' in dommm:
            domain.append(dommm.split('www.',1)[1])

          else:
             domain.append(dommm)
        items_val={'name':name,
        'dis_link':link,
        'description':response.css(".st  ::text").extract_first(),
        'target_url':target_url,
        'review':view}
        print(yield items_val)
        link_next=response.css('a.fl::attr(href)').extract()

          
        for url in response.css('h3.yt-lockup-title > a::attr(href)'):
          print url
          url=response.urljoin(url)
          yield scrapy.Request(url=url,callback=self.parse_details,meta={'items': items_val})
          print(items)


    def parse_details(self,response):
      item_val = response.meta.get('items')
      descri=''

      fetch(url)
      pub_user=response.css('div.yt-user-info >a::text').extract()
      for des in response.css('p#eow-description  ::text').extract():
            descri+=des 

      date_Val=response.css('strong.watch-time-text  ::text').extract()
      item ={
            'descri':descri,
            'image_logo':response.css('img::attr(data-thumb)').extract_first()
            }
      item.update(item_val)
        
      print(yield item)  
      # if item:
      #     check_id=models.execute_kw(dbname, uid, password,
      #             'cw.you_tube_video_table_master', 'search_count',
      #             [[['ad_name','=',item_val['name']] ,['you_video_main_id','=',temp_id],['stage_id','=',key1[0]['id']]]])
      #     if check_id==0:
      #         temp_id2 = models.execute_kw(dbname, uid, password, 'cw.you_tube_video_table_master', 'create', [{
      #                     'name': name,
      #                     'website':url,
      #                     'published_on':date_Val,
      #                     'published_by':pub_user,
      #                     'web':image_logo ,
      #                     'ad_name': name,
      #                     'reviews':review,
      #                     'stage_id':stage_id,
      #                     'you_video_main_id':scrape_id,
                                
      #                   }])
                    
                    
      #         temp_id3 = models.execute_kw(dbname, uid, password, 'cw.you_tube_video_table', 'create', [{
      #                     'name': name,
      #                     'website':url,
      #                     'published_on':date_Val,
      #                     'published_by':pub_user,
      #                     'web':image_logo ,
      #                     'ad_name': name,
      #                     'reviews':review,
      #                     'stage_id':stage_id,
      #                     'you_video_main_id':scrape_id,
      #                   }])
                
      # yield item
    
 