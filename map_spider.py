
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "spione"
    # req = Request('https://www.google.co.in/search?q=prestige+misty+water&newwindow=1&ei=_MUSWvoHi9u-BM3IntgF&start=10&sa=N&biw=1301&bih=678', headers={"header1":"value1"})
    start_urls = [
        'https://www.google.co.in/maps/place/Prestige+Misty+Waters,+4th+Cross+Rd,+Thimakka+Layout,+Coconut+Garden,+Cholanayakanahalli,+Hebbal,+Bengaluru,+Karnataka+560032/@13.0359403,77.5960011,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae17986e19cbb3:0xcfb36765a70d17dc!8m2!3d13.0359403!4d77.5981951?hl=en']

    def parse(self, response):
        self.log("I just visited the :"+response.url)
        print(response.body)
        
