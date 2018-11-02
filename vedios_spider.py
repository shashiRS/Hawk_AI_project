import scrapy
import urllib
class QuotesSpider(scrapy.Spider):
    name = "videospider"
    # req = Request('https://www.google.co.in/search?q=prestige+misty+water&newwindow=1&ei=_MUSWvoHi9u-BM3IntgF&start=10&sa=N&biw=1301&bih=678', headers={"header1":"value1"})
    term='Prestige Misty Waters'
    start_urls = [
    'https://www.google.co.in/search?q='+urllib.quote(term)+'&tbm=vid']

    def parse(self, response):
        name=''
        names=[]
        link=''
        linkq=[]
        description=''
        publish=''
        published_by=[]
        domain=[]
        self.log("I just visited the :"+response.url)
        print(response.body)
        print(response.css('cite.kv::text'))
        # print(response.body)
       
          
        for items in response.css('h3.r >a ::text').extract():
            name+=items
            names.append(items)
        
        for links in response.css('h3.r >a ::attr(href)').extract():
            link+=links
            linkq.append(links)

            dommm=links.split('/',2)[2]
            if 'www' in dommm:
                domai=dommm.split('www.',1)[1]
                domain.append(domai.split('/',1)[0])

            else:
                domain.append(dommm.split('/',1)[0])
        print domain
        print(names)
        print(linkq)

        for desc in response.css('span.st  ::text').extract():
            description+=desc
        print(description)
        
        for pub in response.css('div.slp ::text').extract():
            publish+=pub
            print(pub)
            published_by.append(pub)
        print(published_by)
       