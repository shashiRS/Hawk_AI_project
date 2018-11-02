import scrapy

class QuotesSpider(scrapy.Spider):
    name = "spione"
    # req = Request('https://www.google.co.in/search?q=prestige+misty+water&newwindow=1&ei=_MUSWvoHi9u-BM3IntgF&start=10&sa=N&biw=1301&bih=678', headers={"header1":"value1"})
    start_urls = [
        'https://www.google.co.in/search?q=brigade+cosmopolis']

    def parse(self, response):
        print(response.body)
        self.log("I just visited the :"+response.url)
        for quote in response.css('li.ads-ad'):
            print(quote)
            item={
            
            'link':quote.css('h3.ellip>a::attr(href)').extract(),
            'name':quote.css('h3.ellip>a::text').extract(),
            'display_url':quote.css('cite._WGk::text').extract(),
            'addescription':quote.css('div.ellip::text').extract(),

            # 'page':response.css('a.fl::text').extract(),
            }
            yield item
      
        next_page_url=response.css('a.fl::attr(href)').extract_first(),
        next_page_url=response.urljoin(next_page_url)
        yield scrapy.Request(url=next_page_url,callback=self.parse)


       #  new=Orgnz(link=link[i],orname_desc=orname_des[i])   
       #  db.session.add(new)
       #  db.session.commit()
       # 