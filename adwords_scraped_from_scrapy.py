import scrapy
from scrapy.crawler import CrawlerProcess
class MySpider1(scrapy.Spider):
	name="spider_adwords"
	print("spider_adwords")
	allowed_domains = ["izito.co.in"]
	def __init__(self, name=None, *args, **kwargs):
		self.start_urls = ["http://www.izito.co.in/ws?q=brigade%20whitefield&asid=iz_in_gb_2_cg1_10&mt=b&nw=s&de=c&ap=1t3"]
       
        
        def parse(self, response):
	        items_val={}
	        print(response.body)