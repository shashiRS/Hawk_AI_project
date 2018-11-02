# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.http import FormRequest
import pdb
import re
import collections
import csv


class SeodataSpider(scrapy.Spider):
    name = 'seodata'
    allowed_domains = ['serplab.co.uk']
    login_url='https://www.serplab.co.uk/process/login.php'
    start_urls = [login_url]
    item=[]
    itm=[]
    def parse(self, response):
        crf_token=response.css('input[name="token"]::attr(value)').extract()
        print(crf_token)
        data={
        'token':crf_token,
        'user-email':'Whitefieldapts@gmail.com',
        'user-pw': 'apartments456',
        }
        yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.parse_q)
    
    def parse_q(self,response):
        print(response.css('div.table-responsive >table >tbody >tr >td.clickable >span.filterable ::text').extract())        
        ids=response.css('div.table-responsive >table >tbody >tr ::attr(data-projectid)').extract()
        # https://www.serplab.co.uk/user/project-details.php?id=424991
        for i in ids:
            call_url='https://www.serplab.co.uk/user/project-details.php?id='+str(i)
            yield SplashRequest(call_url, callback=self.parse_details,args={'wait': 0.24})
    def parse_details(self,response):
        d = collections.defaultdict(list)
        lis=[]
        lat=[]
        chg=[]
        bes=[]
        fir=[]
        valu=[]
        name=''
        for n in response.css('div.table-responsive >table >tbody >tr.sort_row'):
            tabledata=n.css(' ::text').extract()
                      
            # for nn in tabledata:
            #     name=unicode(name.strip())+','+unicode(nn.strip())
                
            d['foo'].append(tabledata)  
      
        for llen in range(len(d['foo'])):
            g=d['foo'][llen]
            val=''
            p=[r.encode('utf-8').strip() for r in g]

            for pp in p:
                val=val+','+pp
            strin=re.sub(r'(,)+', ',',val )
            original_data=re.sub(r'^,','',strin)
            self.item.append(original_data)

        # print self.item
        for i in self.item:
            bb=''
            bb=i
            bvalue=bb.split(',')
            lis.append(bvalue[1])
            chg.append(bvalue[2])
            lat.append(bvalue[3])
            bes.append(bvalue[4])
            fir.append(bvalue[5])
            valu.append(bvalue[6])

        itemss={
        'Keyword_url':response.url,
        # 'keyword':self.item,
        'key_name':lis,
        'change':chg,
        'latest':lat,
        'best':bes,
        'first':fir,
        'volume':valu,

        # 'name':[lat],
        }
            # with open('dict.csv', 'wb') as csv_file:
            #     writer = csv.writer(csv_file)
            #     for key, value in itemss.items():
            #         writer.writerow([key, value])
            # self.itm.append(itemss)
        # print(self.itm)
        # ele={}
        for key, value in itemss.items():
            print([key, value])
            ele={
            "keys":key[0],
            "values":value[0],
            }
        # for i in itemss:
        #     print(itemss[i])
        yield self.item