# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["qoutes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/login',
    )

    def parse(self, response):
    	print("Hello------------")
    	csrf_token=response.xpath('//*[@name="csrf_token"]/@value').extract()
    	csrf_token1=''
    	for i in csrf_token:
    		csrf_token1=i
    	formdata={'csrf_token':csrf_token1,'username':'shashi','password':'Shashi'}
    	print(FormRequest('http://quotes.toscrape.com/login',formdata={'csrf_token':csrf_token1,'username':'shashi','password':'Shashi'},callback=self.parse_after_login))
        yield FormRequest('http://quotes.toscrape.com/login',callback=self.parse_after_login,formdata=formdata)
    def parse_after_login(self,response):
    	print("U in!")
    	if response.xpath('//a[text()="Logout"]'):
    		self.log("U logged in!")
