import scrapy
import urllib
class QuotesSpider(scrapy.Spider):
    name = "spione"
    # req = Request('https://www.google.co.in/search?q=prestige+misty+water&newwindow=1&ei=_MUSWvoHi9u-BM3IntgF&start=10&sa=N&biw=1301&bih=678', headers={"header1":"value1"})
    term=raw_input("Enter the project name: ")
    start_urls = [
    'https://www.google.co.in/search?q='+urllib.quote(term)+'&tbm=vid']

    def parse(self, response):
        name=''
        link=''
        description=''
        publish=''
        domain=''
        self.log("I just visited the :"+response.url)
        
        print(response.css('cite.kv::text'))
        # print(response.body)
       
          
        for items in response.css('h3.r >a ::text').extract_first():
            name+=items
        for links in response.css('h3.r >a ::attr(href)').extract_first():
            link+=links
            dom=links.split('.',1)[1]
            domain=dom.split('/',1)

        for desc in response.css('span.st  ::text').extract():
            description+=desc
        for pub in response.css('span.f ::text').extract():
            publish+=pub
       