# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import pdb
import time
import json
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.http import FormRequest
from collections import OrderedDict
import pandas
import re
import csv

class AnalysistoolqSpider(scrapy.Spider):
    name = 'analysistoolq'
    allowed_domains = ['magicbricks.com']
    #http_user = 'b37dba23d8f647a7bbce8dd0b786b3ff' 
    item = OrderedDict()

    def __init__(self, *args, **kwargs):
        self.dict_val={}
        self.start_url=[]
        self.item_list=[]
        self.item_list2=[]
        self.localit=['Mysore road',
        'kengeri']
        j=0
        for i in range(1,5):
            if i==1:
                j=1
            else:
                j=2
            for loc in self.localit:
                print loc
                url='https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?proptype=Multistorey-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa,Residential-Plot&Locality=%s&cityName=Bangalore&price=Y&page=%s&bar_propertyType_new=10002_10021_10022_10020,10001_10017,10000&mbTrackSrc=tabChange&tab%sProject=property'%(loc,i,j)
                self.start_url.append(url)
               
           
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                super(AnalysistoolqSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
       
        for url in self.start_url:
            yield scrapy.Request(url, callback=self.parse_details,
                                    errback=self.errback_httpbin,
                                    dont_filter=True)
            #yield SplashRequest(url, self.parse_details,  args={'wait': 0.5})
            #yield scrapy.Request(url=url,callback=self.parse_details)
    
    def parse_details(self,response):
        item={}
       
        #data = json.loads(response.body)
        print(response.status)
        val1=response.css('div.errorMsgBlock::attr(id)').extract()
        val=[s.split('errorCheckBox')[1].split('_C')[0] for s in val1]
        val=[s.split('_P')[0] for s in val]
        val=[s.split('_I')[0] for s in val]
        #
        #for values in val:
        #self.val=values
        #print(self.val)
        i=0
        
        link_list=[]
        for d1 in response.css('div.srpBlockTopRow'):
            self.val=val[i]
            print(self.val)
            i+=1
            author=''
            for item1 in d1.css('p.proHeading ::text').extract():

                author+=item1.strip()
            link=response.urljoin(d1.css('div.proNameColm1 > a::attr(href)').extract_first())
            proj_loc=''
            proj_city=''
            try:
                for item1 in d1.css('div.proNameColm1 >p.proGroup::text').extract():
                    # pdb.set_trace()
                    da=item1.strip().split('in')[1]
                    proj_loc+=da.split(',')[0].strip()
                    proj_city+= da.split(',')[1].strip()
            except:
                pass
            
            project_by=d1.css('div.proNameColm1 >p.proGroup >span::text').extract_first()
            
            item={
            'Title':author,
            'link':link,
            'id':self.val,
            'builder':project_by,
            'possessiondate':response.css('div.posByCons ::text').extract_first().strip(),
            # 'lat_lng':response.css('p.seeOnMapLink >a::attr(onclick)').extract_first().split('html?')[1].split('&')[:2],
            'project_location':proj_loc,
            'Project_City':proj_city,
            'address':proj_loc,
            'latitude':response.css('p.seeOnMapLink >a::attr(onclick)').extract_first().split('html?')[1].split('&')[:2][0].split('=')[1].strip(),
            'longitude':response.css('p.seeOnMapLink >a::attr(onclick)').extract_first().split('html?')[1].split('&')[:2][1].split('=')[1].strip(),
            'micro_locality':proj_loc,
            }
            link_list.append(item)
        
        
        if link_list:
            for item_link in link_list:
                yield scrapy.Request(item_link['link'],callback=self.fetch_detail,errback=self.errback_httpbin,meta={'items_val': item_link})
                #yield SplashRequest(item_link['link'], self.fetch_detail,meta={'items_val': item_link})
                    
    def fetch_detail(self,response):
        
        items = response.meta.get('items_val')
        # pdb.set_trace()
        # locality_id=response.css('div#projectNearByList >script::text').extract()[0].strip().split('&localityId')[1].split('&cityId')[0].split('=')[1]
        locality_id=1
        #unit_starting_price=''
        #unit_ending_price=''
        #SQFT_starting_price=''
        #SQFT_ending_price=''
        units=''
        towers=''
        unit=''
        bed=''
        space=''
        pro_title=''
        pro_detail=''
        about_project=''
        status=response.css('div.newChildBlock > div >div >div.secValueUp ::text').extract_first()
        col_final=[]
        header=['Unit Type','Build-Up Area','Price_per_sqft','Price']
        
        col=[]
        for x in response.css('div.topAdvListLi >div.propertyListCont'):
            col_list=[]
            for x1 in x.css('div >div >div.propertyListNTD '):
                col_val=''
                for val in x1.css('div ::text').extract():
                    col_val+=val
                col_list.append(col_val)
            col.append(col_list)
        for x3 in col:
            col_semi=[]
            final_dict={}
            for i in range(0,len(header)):
                z={}
                z={header[i]:x3[i]}
                final_dict.update(z)
            col_semi.append(final_dict)
            col_final.append(col_semi)    
        if response.css('div#otherProjectsByDeveloper ::text').extract():
            about_project='https://www.magicbricks.com/propertyDetails/otherProjectsByDeveloper.html?'+str(response.css('div#otherProjectsByDeveloper ::text').extract()[1].split('.html?')[1].strip().split('";')[0])
        
        
        project_description=''
        project_highlights=''
        rera_no=response.css('div.projLBlock >div.c_dark_gray ::text').extract_first()
        for x in response.css('div.projLBlock div.project_Description ::text').extract():
            project_description+=x
            
        for x in response.css('div.projLBlock div.tbl div.tbl-td ::text').extract():
            project_highlights+=x
        
        value_amn_list=[]
        for x in response.css('div.amenitiesBlock >ul >li'):
            values_amenities=''
            for x1 in x.css('li ::text').extract():
                values_amenities+=x1
            value_amn_list.append(values_amenities)
        final_val_amn=''        
        for i in range(0,len(value_amn_list)):
            z=i+1
            final_val_amn+=str(z)+'. '+value_amn_list[i]
        
        price_list=[]
        for x1 in response.css('div#tabs-sale >ul >li'):
            dict_val={}
            unit_type=''
            build_up_area=''
            headers=x1.css('div.left-contain >div.details >p >span::text').extract()
            headers=[z.strip() for z in headers]
            for x in x1.css('div.left-contain >div.head::text').extract():
                unit_type+=x
            for x in x1.css('div.left-contain >div.head >span::text').extract():
                build_up_area+=x
            temp=[]    
            for x in x1.css('div.left-contain >div.details >p'):
                val=''
                for x2 in x.css('p::text').extract():
                    val+=x2
                temp.append(val)  
            
            col_semi=[]
            final_dict={}
            for i in range(0,len(temp)):
                z={}
                z={headers[i]:temp[i]}
                final_dict.update(z)
            description=''
            try:
                for item_val in x1.css('div.localText >div.minShow.project_Description >p ::text').extract()[1]:
                    description+=item_val
            except:
                for item_val in x1.css('div.localText >div.minShow.project_Description ::text').extract():
                    description+=item_val  
            total_price=''
            pri_range=''
            p_per_sqft=''
            total_price=x1.css('div.right-contain div.head ::text').extract_first().strip() if x1.css('div.right-contain div.head ::text').extract_first() else ''
            price_per_sqft=x1.css('div.right-contain div.sqrPrice >span.sqrPriceField ::text').extract_first().strip() if x1.css('div.right-contain div.sqrPrice >span.sqrPriceField ::text').extract_first() else ''
            for i in response.css('td.newPiceBlockSec >div.secValueUp ::text').extract():
                ranges=i.strip().split('0xe2')
                for i in ranges:
                    pri_range+=i
            for i in response.css('td.newPiceBlockSec >div.secSubUp ::text').extract():
                da=i.strip().split('(')[1]
                p_per_sqft+=da.split(')')[0]

                # pdb.set_trace()
                # print(re.sub(r'[^\u20b9]+','', ranges))


            self.dict_val={
                'unit_type':unit_type,
                'build_up_area':build_up_area,
                'projectstatus':final_dict['Status'].split('(')[0].strip(),
                'Short Description':description,
                'total_price':total_price,
                'price_per_sqft':p_per_sqft,
                'Price_range':pri_range,
                }
            # pdb.set_trace()
            # price_list.append(dict_val)        
        #for d1 in response.css('div.secValueUp::text').extract():
            #value=d1.split('-')
            #if len(value)==2:
                #unit_starting_price+=value[0]
                #unit_ending_price+=value[1]
            #else:
                #unit_starting_price+=value[0]

        #for d1 in response.css('div.secSubUp::text').extract():
            #value=d1.split('-')
            #if len(value)==2:
                #SQFT_starting_price+=value[0]
                #SQFT_ending_price+=value[1]
            #else:
                #SQFT_starting_price+=value[0]
            
        for d1 in response.css('div.infoList ::text').extract():
            unit+=d1
        try:
            units=unit.split('\n')[1]
            towers=unit.split('\n')[2]
        except:
            pass

        
        update_list=[]
        valuess=[]
        
        val1=''
        val2=''
        val3=''
        val4=''
        val5=''
        
        for x in response.css('div.unitSlide >ul >li'):
            unit_type=''
            build=''
            unit_price=''
            unit_type=x.css('li >div.propDtls >div.bed ::text').extract_first()
            build=x.css('li >div.propDtls >div.space ::text').extract_first()
            # valuess.append(','+''.join([i for i in build if i not in 'sqft']))

            if '1 BHK Flat' in unit_type:
                if val1=='':
                    val1+=''.join([i for i in build if i not in 'sqft'])
                else:
                    val1+=','+''.join([i for i in build if i not in 'sqft'])
                    # writer.writerow({'1 BHK Flat': val})
            elif '2 BHK Flat' in unit_type:
                if val2=='':
                    val2+=''.join([i for i in build if i not in 'sqft'])
                else:
                    val2+=','+''.join([i for i in build if i not in 'sqft'])
                # writer.writerow({'2 BHK Flat': val})
            elif '3 BHK Flat' in unit_type:
                if val3=='':
                    val3+=''.join([i for i in build if i not in 'sqft'])
                else:
                    val3+=','+''.join([i for i in build if i not in 'sqft'])
                # writer.writerow({'3 BHK Flat': val})
            elif '4 BHK Flat' in unit_type:
                if val4=='':
                    val4+=''.join([i for i in build if i not in 'sqft'])
                else:
                    val4+=','+''.join([i for i in build if i not in 'sqft'])
                # writer.writerow({'4 BHK Flat': val})
            elif '5 BHK Flat' in unit_type:
                if val5=='':
                    val5+=''.join([i for i in build if i not in 'sqft'])
                else:
                    val5+=','+''.join([i for i in build if i not in 'sqft'])
                # writer.writerow({'5 BHK Flat': val})





            # out=open('exam1.csv', 'a')
            # fieldnames = ['1 BHK Flat','2 BHK Flat','3 BHK Flat','4 BHK Flat','5 BHK Flat']
            # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            # writer.writerow({'1 BHK Flat': val1,'2 BHK Flat': val2,'3 BHK Flat': val3,'4 BHK Flat': val4,'5 BHK Flat': val5})
            
                # if '2 BHK Flat' in unit_type:
                #     with open('exam.csv', 'a') as csvfile:
                #         fieldnames = ['2 BHK Flat']
                #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #         writer.writeheader()
                #         writer.writerow({'2 BHK Flat': build})
            unit_price='('+unit_type +'->'+build+')'
            update_list.append(unit_price)
            price_per_SQFT=x.css('div.topAdvListLi >div.propertyListCont >div>div>div.propertyListNTD.tw2').extract_first()
        unit_price_final=''    
        for z in  range(0,len(update_list)):
            unit_price_final+=update_list[z] + (' ' if (len(update_list)-1)==z else ', ')
        #for d in response.css('div.bed ::text').extract():
            #bed+=d
        #for d in response.css('div.space ::text').extract():
            #space+=d
        #for d1 in response.css('div.proMHeading ::text').extract():
            #pro_title+=d1

        for d1 in response.css('div.localText ::text').extract():
            pro_detail+=d1
        
        #for s in response.css('div.localText ::text').extract():
            #about_project+=s
        # pdb.set_trace()
        # unit_price_final.split(',')
        
        item={
             'units':units,
             'towers':towers,
             'unit_price':unit_price_final,
             
             'about_project':about_project,
             'table':col_final,
             # 'Project Status':status,
             # 'property_deatils':self.dict_val,
             'Super Built Area':self.dict_val['build_up_area'],
             'Price Range':self.dict_val['Price_range'],
             'Price Per Sq Ft':self.dict_val['price_per_sqft'],
             # 'Description':self.dict_val['description'],
             'Bedrooms':self.dict_val['unit_type'],
             'project_description':project_description,
             'project_highlights':project_highlights,
             'final_val_amn':final_val_amn,
             'rera_no':rera_no,
             'specification':response.css('div.projLBlock >div.constUpdate >div.consUpdateBlock >div.specContainer ::text').extract()

            }
        items.update(item)
        dic = {'1 BHK Flat':val1,'2 BHK Flat':val2,'3 BHK Flat':val3,'4 BHK Flat':val4,'5 BHK Flat':val5}
        download_dir = "exampleCsv.csv"
        csv = open(download_dir, "w")
        columnTitleRow = "1 BHK Flat, 2 BHK Flat,3 BHK Flat,4 BHK Flat,5 BHK Flat\n"
        csv.write(columnTitleRow)
        for key in dic.keys():
            # key = dic[key]
            row = key + "," + dic[key] + "\n"
            csv.write(row)
            pdb.set_trace()
        
        #self.item_list.append(items)
        #for values in self.item_list:
       
        #yield items
        
        yield scrapy.Request('http://www.magicbricks.com/propertyDetails/Project-Rates-Trends-Month?psmid='+items['id']+'&propType=10002&localityid=%s&localityName=%s'%(locality_id,self.name), callback=self.project_history,errback=self.errback_httpbin,meta={'items_val': items})
        #if item['about_project']:
            #yield scrapy.Request(items['about_project'],callback=self.about_project,errback=self.errback_httpbin,meta={'items_val': items})

    def project_history(self,response):
        # pdb.set_trace()
        item = response.meta.get('items_val')
        count=0
        count+=1
        print(count)
        price_trend=''
        col_final=[]
        header=[]
        header=response.css('div#priceTable >table >thead >tr >td::text').extract()
        header=[z.strip() for z in header]
        col=[]
        for x in response.css('div#priceTable >table >tbody >tr'):
            col_list=[]
            for x1 in x.css('td'):
                col_val=''
                for val in x1.css('td ::text').extract():
                    col_val+=val
                col_list.append(col_val.strip())
            col_list=[z for z in col_list if z]
            col_list=[z for z in col_list if z!='Lowest' and z!='Highest']
           
            col.append(col_list)
        for x3 in col:
            col_semi=[]
            final_dict={}
            for i in range(0,len(header)):
                z={}
                z={header[i]:x3[i]}
                final_dict.update(z)
                
            col_semi.append(final_dict)
            col_final.append(col_semi)  
            
            
        for s in response.css('div.priceTrendDetailContnet ::text').extract():                  
            price_trend+=s
        
            
        item1={
        'price_trend':col_final,

        
        }
        item.update(item1)
        
        #self.item_list2.append(item)
        #for values in self.item_list2:
        #print(item['about_project'])
        if item['about_project']:
            for req in self.self_check(item['about_project'],item):
                val=yield req
                
            #item.update(item3)
            #yield item
            #yield scrapy.Request(item['about_project'],callback=self.about_project,errback=self.errback_httpbin,meta={'items_val': item})
        else:
            item2={
            'about_project_details':'',
            'about_builder':'',

            
            }
            item.update(item2)
            yield item
            
            
    def self_check(self,link,item):
        
        yield FormRequest(link,callback=self.about_project,errback=self.errback_httpbin,meta={'items_val': item})

    def about_project(self,response):
        
        item = response.meta.get('items_val')
        
        about_project1=''
        about_list=[]
        for x in response.css('div.devDataBlock >div.devDBlock'):
            about={}
            about_builder=''
            for values in x.css('div::text').extract():
                about_builder+=values+' '
            about={'value':about_builder.strip()}
            about_list.append(about)
        for s in response.css('div#aboutMore ::text').extract():
            about_project1+=s
        item2={
            'about_project_details':about_project1,
            'about_builder':about_list,
            }
        item.update(item2)
        pdb.set_trace()
        # df=pandas.DataFrame(item)
        # df.to_csv("dfTest.txt","\t",header=True,cols=["b","a","c"], engine='python')

        # print(df.to_csv("dfTest.txt","\t",header=True,column=["author","project_by","location","self.dict_val['build_up_area']"], engine='python'))

        # yield item
        # print self.dict_val

        
        # print item['author']
        # print item['location']
        yield item

        
        
    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)     
        
        #last day work (response.css('div#otherProjectsByDeveloper ::text').extract()[1].split('&cityName'))[0].strip()