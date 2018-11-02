import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider1(scrapy.Spider):
	name="spider1"
	print("spiderone")
	allowed_domains = ["google.co.in"]
	def __init__(self, name=None, *args, **kwargs):
		term='Buy Laptop online'
        self.start_urls = ['https://www.google.co.in/search?q=%s'%(urllib.quote(term))]
       
        super(HalkSpider, self).__init__(*args, **kwargs)
        def parse(self, response):
	        items_val={}
	        for q1 in response.css('li.ads-ad'):
	            

	            name=''
	            link=''
	            domain=''
	            for items in q1.css('h3.ellip >a  ::text').extract():
	                name+=items
	            for links in q1.css('cite._WGk  ::text').extract():
	                link+=links
	            res=link.split('/',1)[0]
	            domain=res.split(".", 1)[1]
	            
	            target_url=response.urljoin(q1.css("h3.ellip > a::attr(href)").extract_first())
	            
	            items_val={
	                'name':name,
	                   'dis_link':link,
	                   'description':q1.css(".ads-creative  ::text").extract_first(),
	                   'target_url':target_url,
	                   'domain':domain
	                }
	                        
	            print(name)    
	            print("-------------------------")
	            yield items_val
	            
      

    def parse_details(self,response):
        item={}
        for q1 in response.css('li.ads-ad'):
            name=''
            link=''
            for items in q1.css('h3.ellip > a   ::text').extract():
                name+=items
                
            for links in q1.css('cite._WGk  ::text').extract():
                link+=links
            res=link.split('/',1)[0]
            domain=res.split(".", 1)[1]
            
            target_url=response.urljoin(q1.css("h3.ellip > a::attr(href)").extract_first())
            item={'name':name,
                   'dis_link':link,
                   'description':q1.css(".ads-creative  ::text").extract_first(),
                   'target_url':target_url,
                    'domain':domain

                }
       
        
            
            
                
            yield item
   

class MySpider2(scrapy.Spider):
	name="spider2"
	print("spidertwo")
	allowed_domains = ["google.co.in"]
    
    
    def __init__(self, name=None, *args, **kwargs):
        term='Find Apartments for sale'
        self.start_urls = ['https://www.google.co.in/search?q=%s'%(urllib.quote(term))]
       
        super(HalkSpider, self).__init__(*args, **kwargs)

        #temp_id = models.execute_kw(dbname, uid, password, 'cw.test.module', 'create', [{
                #'name':13,
                #'stage_id':key1[0]['id']
                
                
                #}])

    def parse(self, response):
        items_val={}
        for q1 in response.css('li.ads-ad'):
            

            name=''
            link=''
            domain=''
            for items in q1.css('h3.ellip >a  ::text').extract():
                name+=items
            for links in q1.css('cite._WGk  ::text').extract():
                link+=links
            res=link.split('/',1)[0]
            domain=res.split(".", 1)[1]
            
            target_url=response.urljoin(q1.css("h3.ellip > a::attr(href)").extract_first())
            
            items_val={
                'name':name,
                   'dis_link':link,
                   'description':q1.css(".ads-creative  ::text").extract_first(),
                   'target_url':target_url,
                   'domain':domain
                }
                        
            print(name)    
            print("-------------------------")
            yield items_val
            
            
             
        #link_next=response.css('a.fl::attr(href)').extract()
        #link_next2=[item for item in link_next if 'start=' in item]
        #for i in range(1,5):
            #url=link_next2[i]
            #url=response.urljoin(url)
            #yield scrapy.Request(url=url,callback=self.parse_details)
           
            
           
   
   

    def parse_details(self,response):
        item={}
        for q1 in response.css('li.ads-ad'):
            name=''
            link=''
            for items in q1.css('h3.ellip > a   ::text').extract():
                name+=items
                
            for links in q1.css('cite._WGk  ::text').extract():
                link+=links
            res=link.split('/',1)[0]
            domain=res.split(".", 1)[1]
            
            target_url=response.urljoin(q1.css("h3.ellip > a::attr(href)").extract_first())
            item={'name':name,
                   'dis_link':link,
                   'description':q1.css(".ads-creative  ::text").extract_first(),
                   'target_url':target_url,
                    'domain':domain

                }
       
        
            
            
                
            yield item
    
class MySpider3(scrapy.Spider):
	name="spider3"
	print("spiderthree")
	allowed_domains = ["google.co.in"]
    
    
    def __init__(self, name=None, *args, **kwargs):
        term='Buy CRM software'
        self.start_urls = ['https://www.google.co.in/search?q=%s'%(urllib.quote(term))]
       
        super(HalkSpider, self).__init__(*args, **kwargs)

        #temp_id = models.execute_kw(dbname, uid, password, 'cw.test.module', 'create', [{
                #'name':13,
                #'stage_id':key1[0]['id']
                
                
                #}])

    def parse(self, response):
        items_val={}
        for q1 in response.css('li.ads-ad'):
            

            name=''
            link=''
            domain=''
            for items in q1.css('h3.ellip >a  ::text').extract():
                name+=items
            for links in q1.css('cite._WGk  ::text').extract():
                link+=links
            res=link.split('/',1)[0]
            domain=res.split(".", 1)[1]
            
            target_url=response.urljoin(q1.css("h3.ellip > a::attr(href)").extract_first())
            
            items_val={
                'name':name,
                   'dis_link':link,
                   'description':q1.css(".ads-creative  ::text").extract_first(),
                   'target_url':target_url,
                   'domain':domain
                }
                        
            print(name)    
            print("-------------------------")
            yield items_val
            
            
             
        #link_next=response.css('a.fl::attr(href)').extract()
        #link_next2=[item for item in link_next if 'start=' in item]
        #for i in range(1,5):
            #url=link_next2[i]
            #url=response.urljoin(url)
            #yield scrapy.Request(url=url,callback=self.parse_details)
           
            
           
   
   

    def parse_details(self,response):
        item={}
        for q1 in response.css('li.ads-ad'):
            name=''
            link=''
            for items in q1.css('h3.ellip > a   ::text').extract():
                name+=items
                
            for links in q1.css('cite._WGk  ::text').extract():
                link+=links
            res=link.split('/',1)[0]
            domain=res.split(".", 1)[1]
            
            target_url=response.urljoin(q1.css("h3.ellip > a::attr(href)").extract_first())
            item={'name':name,
                   'dis_link':link,
                   'description':q1.css(".ads-creative  ::text").extract_first(),
                   'target_url':target_url,
                    'domain':domain

                }
       
        
                
            yield item
    

process = CrawlerProcess()
process.crawl(MySpider1)
process.crawl(MySpider2)
process.crawl(MySpider3)
process.start() # the script will block here until all crawling jobs are finished