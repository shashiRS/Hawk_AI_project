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


class VillaresultPySpider(scrapy.Spider):
    name = 'villaresult.py'
    allowed_domains = ['magicbricks.com']
    #http_user = 'b37dba23d8f647a7bbce8dd0b786b3ff' 
    item = OrderedDict()

    def __init__(self, *args, **kwargs):
        self.dict_val={}
        self.start_url=[]
        self.item_list=[]
        self.item_list2=[]
        self.localit=['Whitefield',
     'Sarjapur Road',
     'Electronic City Phase I',
     'Marathahalli',
     'HSR Layout',
     'Koramangala',
     'Bellandur',
     'Bannerghatta Road',
     'Mahadevapura',
     'JP Nagar',
     'BTM Layout',
     'BTM Layout',
     'Doddenakundi',
     'Kanakapura Road',
     'Indira Nagar',
     'K R Puram',
     'Brookefield',
     'Thanisandra Main Road',
     'Yelahanka',
     'Hennur',
     'Horamavu',
     'Ramamurthy Nagar',
     'Jayanagar',
     'Hosur Road',
     'Panathur',
     'Electronic City Phase II',
     'Hebbal',
     'Kundalahalli',
     'Marathahalli-Sarjapur Outer Ring Road',
     'Kaggadasapura',
     'CV Raman Nagar',
     'Banashankari',
     'Hosa Road',
     'Old Airport Road',
     'Old Madras Road',
     'Budigere',
     'Hoodi',
     'Off Sarjapur road',
     'Varthur',
     'Sarjapur',
     'Harlur',
     'Rajaji Nagar',
     'Bommanahalli',
     'Haralur Road',
     'Kadugodi',
     'HBR Layout',
     'Raja Rajeshwari Nagar',
     'Kasturi Nagar',
     'Yeshwanthpur',
     'Domlur',
     'Vijayanagar',
     'Kalyan Nagar',
     'Thubarahalli',
     'RT Nagar',
     'Banaswadi',
     'Begur Road',
     'Kasavanahalli',
     'Bilekahalli',
     'Malleshwaram',
     'Chandapura',
     'Yelahanka New Town',
     'Vidyaranyapura',
     'Thanisandra',
     'Hennur',
     'AECS Layout',
     'Devanahalli',
     'Ulsoor',
     'Chandapura Anekal Road',
     'Kadubeesanahalli',
     'Begur',
     'Marathahalli ORR',
     'Doddaballapur Road',
     'Jalahalli West',
     'Mysore Road',
     'Sahakara Nagar',
     'Jakkur',
     'Bellandur Outer Ring Road',
     'Basaveshwara Nagar',
     'Murugeshpalya',
     'Uttarahalli',
     'HSR Layout Sector 2',
     'Munnekollal',
     'JP Nagar Phase 8',
     'Basavanagudi',
     'JP Nagar Phase 7',
     'Tumkur Road',
     'Ejipura',
     'Nagarbhavi',
     'Singasandra',
     'Mathikere',
     'Kudlu Gate',
     'Hoskote',
     'Jigani',
     'Sarjapur Attibele Road',
     'kaikondrahalli',
     'Arekere',
     'HSR Layout Sector 1',
     'TC Palya Road',
     'Whitefield Road',
     'Shigehalli',
     'Sanjay Nagar',
     'ITPL Road',
     'Kammanahalli',
     'New Thippasandra',
     'HRBR Layout',
     'Kodigehalli',
     'Chansandra',
     'Kengeri',
     'Gunjur',
     'Nagavara',
     'Babusa Palya',
     'Hulimavu',
     'Tavarekere-BTM',
     'Wilson Garden',
     'Frazer Town',
     'HSR Layout Sector 3',
     'HSR Layout Sector 7',
     'JP Nagar Phase 5',
     'Outer Ring Road',
     'JP Nagar Phase 6',
     'Nelamangala',
     'Vishweshwaraiah Layout',
     'Richmond Town',
     'Bommasandra',
     'Banashankari 3rd Stage',
     'BEML Layout',
     'MS Palya',
     'Kodihalli',
     'Pai Layout',
     'Gottigere',
     'Cooke Town',
     'Kumaraswamy Layout',
     'Seegehalli',
     'GM Palya',
     'Devarachikkanahalli',
     'Malleshpalya',
     'Magadi Road',
     'Attibele',
     'Anjanapura',
     'Kalkere',
     'Kengeri Satellite Town',
     'Vignana Nagar',
     'Padmanabha Nagar',
     'RMV 2nd Stage',
     'Cox Town',
     'B Narayanapura',
     'Benson Town',
     'Akshayanagar',
     'Victoria Layout',
     'Kodichikkanahalli',
     'Basavanagar',
     'Dommasandra',
     'Varthur Road',
     'Lingarajapuram',
     'Mahalakshmi Layout',
     'Silk Board',
     'JP Nagar Phase 9',
     'Nagondanahalli',
     'Anekal',
     'Yemalur',
     'Hebbal Kempapura',
     'Kothanur',
     'JP Nagar Phase 1',
     'Bagaluru',
     'Shanthi Nagar',
     'Basapura',
     'Maruthi Sevanagar',
     'Doddakannalli',
     'HAL Layout',
     'JP Nagar Phase 2',
     'Horamavu Agara',
     'OMBR Layout',
     'Aavalahalli',
     'Bannerghatta',
     'Vasanth Nagar',
     'Battarahalli',
     'Kudlu',
     'Kathriguppe',
     'Thavarekere-Magadi Road',
     'Bhoganhalli',
     'Jeevanbheema Nagar',
     'Hanumantha Nagar',
     'Hegde Nagar',
     'Amrutha Halli',
     'MG Road',
     'Devanahalli Road',
     'IVC Road',
     'Margondanahalli',
     'Dasarahalli Hebbal',
     'Srinivasa Nagar',
     'Kaval Byrasandra',
     'Abbigere',
     'Kanaka Nagar',
     'Rachenahalli',
     'Adugodi',
     'Chandra Layout',
     'LB Shastri Nagar',
     'Chikka Banaswadi',
     'Bennigana Halli',
     'New BEL Road',
     'Belathur',
     'Girinagar',
     'Ganga Nagar',
     'Hoskote Malur Road',
     'Sarjapur Bagalur Road',
     'Kogilu',
     'Hongasandra',
     'International Airport Road',
     'Konanakunte',
     'Doddathoguru',
     'Wind Tunnel Road',
     'Panduranga Nagar',
     'Chinnapanna Halli',
     'Shivaji Nagar',
     'ISRO Layout',
     'Madiwala',
     'Siddapura',
     'Peenya',
     'Chamarajpet',
     'Sadashiva Nagar',
     'Nandini Layout',
     'Bellary Road',
     'Mico Layout',
     'Vijaya Bank Colony',
     'HSR Layout Sector 5',
     'Seshadripuram',
     'Ananth Nagar',
     'Richmond Road',
     'Garvebhavi Palya',
     'Immadihalli',
     'Srinagar',
     'Sompura',
     'Jakkasandra',
     'Chikkalasandra',
     'Jayamahal',
     'Dollars Colony',
     'Kempapura',
     'Dodda Banasvadi',
     'Nandi Hills',
     'Choodasandra',
     'Majestic',
     'Cambridge Layout',
     'Kammasandra',
     'Hesaraghatta',
     'Roopena Agrahara',
     'Rajanukunte',
     'Jakkuru Layout',
     'RMV Extension',
     'T Dasarahalli',
     'HSR Layout Sector 6',
     'JP Nagar Phase 4',
     'HAL Layout2',
     'Lavelle Road',
     'Maruthi Nagar',
     'Budigere Road',
     'Nagasandra',
     'Ramagondanahalli',
     'Chikbanavara',
     'Infantry Road',
     'Jalahalli Cross',
     'Byrathi',
     'Jagadish Nagar',
     'Hosakerehalli',
     'Subramanyapura',
     'Neeladri Nagar',
     'Sampangi Rama Nagar',
     'NRI Layout',
     'Rayasandra',
     'Laggere',
     'Srirampura',
     'Venkatapura',
     'R.K. Hegde Nagar',
     'Langford Town',
     'Viveka Nagar',
     'Uttarahalli Main Road',
     'Chelekare',
     'Neelasandra',
     'JP Nagar Phase 3',
     'HSR Layout Sector 4',
     'Jagajeevanram Nagar',
     'RMV',
     'BEML Layout Raja Rajeshwari Nagar',
     'Carmelaram',
     'Kartik Nagar',
     'Mallathahalli',
     'Hosapalaya',
     'Thippasandra',
     'Bagepalli',
     'Cunningham Road',
     'Doddabommasandra',
     'Ullal',
     'Dasarahalli Main Road',
     'Vinayaka Layout',
     'Vasanthapura',
     'Sudhama Nagar',
     'Richards Town',
     'Jalahalli East',
     'Kodathi',
     'Doddaballapur',
     'Gattahalli',
     'Balagere',
     'Kamaksipalya',
     'Chikka Tirupathi',
     'Doddakallasandra',
     'Commercial Street',
     'Bidadi',
     'Banashankari 5th Stage',
     'Kadugondanahalli',
     'Andrahalli',
     'Bagalakunte',
     'Chikkaballapur',
     'lal bagh',
     'Gauribidanur',
     'Nagarbhavi Circle',
     'Annapurneshwari Nagar',
     'Gandhi Nagar',
     'Ashok Nagar',
     'Soukya Road',
     'Vittal Mallya Road',
     'Yelachena Halli',
     'Bhuvaneshwari Nagar',
     'Kamanahalli',
     "Teacher's Colony",
     'St. Johns Road',
     'Cholanayakanahalli',
     'Nagadevanahalli',
     'Bidrahalli',
     'Bikasipura',
     'Jangamakote',
     'Sunkadakatte',
     'Chikkajala',
     'Devinagar',
     'Nayanda Halli',
     'Kalena Agrahara',
     'Malur-Hosur Road',
     'Kadabagere',
     'Guttahalli',
     'Attiguppe',
     'Bhoopasandra',
     'Bannerghatta Jigani Road',
     'Sadduguntepalya',
     'Huskur',
     'Thurahalli',
     'Nallurhalli',
     'HMT Layout',
     'Kacharakanahalli',
     'Bileshivale',
     'Maruthi Nagar (Yelahanka)',
     'Shettihalli',
     'Haragadde',
     'K Channasandra',
     'Kannamangala',
     'Byatarayanapura',
     'Talaghattapura',
     'Boyalahalli',
     'Hombegowda Nagar',
     'Rajiv Gandhi Nagar',
     'Kamala Nagar',
     'Doddakammanahalli',
     'Kempegowda Nagar',
     'Attibele - Anekal Road',
     'Kanakapura',
     'Gubalala',
     'Medihalli',
     'Kithiganur',
     'Brigade Road',
     'Jnana Ganga Nagar',
     'Chikkabellandur',
     'Koralur',
     'Kattigenahalli',
     'Dodda Aalada Mara Road',
     'Chikkabidarakallu',
     'Silver Springs Layout',
     'Kaggalipura',
     'Dooravani Nagar',
     'Palace Road',
     'Prashanth Nagar',
     'Nobo Nagar',
     'Kodigehalli - KR Puram',
     'SMV Layout',
     'Suryanagar',
     'Kumbalgodu',
     'Bommenahalli',
     'Munireddy Layout',
     'Chikkathoguru',
     'Baiyyappanahalli',
     'Virupakshapura',
     'Raghavendra Colony',
     'Shankarapura',
     'Jaya Chamarajendra Nagar',
     'Chinnapa Garden',
     'Garudachar Palya',
     'Wheeler Road',
     'Narasapura',
     'Ramohalli',
     'Harohalli',
     'Kolar Road',
     'Anagalapura',
     'Chokkanahalli',
     'Gunjur Mugalur Road',
     'Arasanakunte',
     'Bettahalasur',
     'Chikkakannalli',
     'Kallumantapa',
     'Kothanoor',
     'Sampigehalli',
     'Tilak Nagar',
     'Dayananda Nagar',
     'Bhovi Palya',
     'Chikka Tirupathi Road',
     'Soundarya Layout',
     'Vittal Nagar',
     'Ragavendra Nagar',
     'Sonnenahalli',
     'Chickpet',
     'Haudin Road',
     'Millers Road',
     'Yelanahalli',
     'Defence Colony - Bagalagunte',
     'Race Course Road',
     'Langford Road',
     'Chintamani',
     'Kuthaganahalli',
     'Tharabanahalli',
     'Shanthala Nagar',
     'Chikkagubbi',
     'Pattandur Agrahara',
     'Koppa',
     'Gollahalli',
     'Binny Pete',
     'Kodipur',
     'Lake City',
     'Munireddypalya',
     'Azad Nagar',
     'Rest House Road',
     "Richard's Park",
     'Cottonpete',
     'Dodsworth Layout',
     'Ashirvad Colony',
     'Doddabele',
     'Craig Park Layout',
     'Nelamangala - Chikkaballapura Road',
     'Vaderahalli',
     'Basavanna Nagar',
     'Huttanahalli',
     'Vijaypura',
     'Donnenahalli',
     'Chadalapura',
     'Meenakunte',
     'Lingadheeranahalli',
     'Residency Road',
     'Sidlaghatta',
     'Dabaspete',
     'Kalasipalayam',
     'Somashetti Halli',
     'Chikkanahalli',
     'Kolar-Chikkaballapur Road',
     'Singanahalli',
     'Karuna Nagar',
     'Belatur',
     'Chamundi Nagar',
     'Garden Layout',
     'Sankey Road',
     'Tippenahalli',
     'Bhaktharahalli',
     'Nehru Nagar',
     'Venkateshpuram',
     'Bapuji Nagar',
     'Williams Town',
     'Kammasandra Agrahara',
     'Bikkanahalli',
     'National Highway 207',
     'Kadusonnappanahalli',
     'Solur',
     'Chikkaballapur-Gauribidanur Road',
     'Doddenahalli',
     'Weavers Colony',
     'Hancharahalli',
     'Devasthanagalu',
     'Chikkabasavanapura',
     'Nanjappa Garden',
     'Budihal',
     'Seenappa Layout',
     'CQAL Layout',
     'Shanthi Pura',
     'Lakshmamma Layout',
     'Madhava Nagar',
     'Adakamaranahalli',
     'Vehloli',
     'Hullahalli',
     'Tharaballi',
     'Ganapathihalli',
     'Ballur',
     'Venkatagiri Kote',
     'Kunigal Road',
     'Essel Gardens',
     'S.Medihalli',
     'Koti Hosahalli',
     'Kommaghatta',
     'JP Nagar',
     'Kanakpura',
     'Outer Ring Road']
        j=0
        for i in range(1,5):
            if i==1:
                j=1
            else:
                j=2
            for loc in self.localit:
                print loc
                url='https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?&proptype=Residential-House,Villa&Locality=%s&cityName=Bangalore&price=Y&page=%s&bar_propertyType_new=10002_10021_10022_10020,10001_10017,10000&mbTrackSrc=tabChange&tab%sProject=property'%(loc,i,j)
                self.start_url.append(url)
               
           
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                super(VillaresultPySpider, self).__init__(*args, **kwargs)


    #def parse(self, response):
        
        #for c1 in response.css('div.g'):
            #title=''
            #for item in c1.css('h3.r >a ::text').extract():
                #title+=item
            
            #if  (''.join(self.name_val.upper().split()) in ''.join(title.upper().split()).upper()) :
                #url=c1.css('h3.r >a::attr(href)').extract_first()
                
                #url2=url.split('&sa')
                #url=url2[0].split('q=')[1]
                #yield scrapy.Request(url=url,callback=self.parse_details)
     
   
    
   
    def start_requests(self):
    	# pdb.set_trace()
        #script="""function main(splash)
        #local url = splash.args.url
        #assert(splash:go(url))
        
        #recheck = True

        #html = splash:html()
        #splash:wait(10)
        #while recheck = True:
            #splash:wait(10)
            #html2 = splash:html()
            #if html != html2:
            #pass
            #elif:
            #recheck = False
            #return {
                #html = splash:html(),
                #}"""
        
        #splash_meta = {'splash': {'endpoint': 'execute', 'args': {'wait': 30, 'lua_source': script}}}

        #for url in self.start_urls:
            #yield scrapy.Request(url, self.parse_details, meta=splash_meta)
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

                author+=item1
            link=response.urljoin(d1.css('div.proNameColm1 > a::attr(href)').extract_first())
            location=''
            for item1 in d1.css('div.proNameColm1 >p.proGroup::text').extract():
                location+=item1
            
            project_by=d1.css('div.proNameColm1 >p.proGroup >span::text').extract_first()
            
            item={
            'Project_name':author,
            'link':link,
            'id':self.val,
            'location':location,
            'project_by':project_by,
            'possession_date':response.css('div.posByCons ::text').extract_first(),
            'lat_lng':response.css('p.seeOnMapLink >a::attr(onclick)').extract_first().split('html?')[1].split('&')[:2]
            
            }
            link_list.append(item)
            
        
        
        if link_list:
            for item_link in link_list:
                yield scrapy.Request(item_link['link'],callback=self.fetch_detail,errback=self.errback_httpbin,meta={'items_val': item_link})
                #yield SplashRequest(item_link['link'], self.fetch_detail,meta={'items_val': item_link})
                    
    def fetch_detail(self,response):
        
        items = response.meta.get('items_val')
        locality_id=response.css('div#projectNearByList >script::text').extract()[0].strip().split('&localityId')[1].split('&cityId')[0].split('=')[1]
        
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
            for item_val in x1.css('div.left-contain >div.details >div.desBlock ::text').extract():
                description+=item_val
                    
            total_price=''
            
            total_price=x1.css('div.right-contain div.head ::text').extract_first().strip() if x1.css('div.right-contain div.head ::text').extract_first() else ''
            price_per_sqft=x1.css('div.right-contain div.sqrPrice >span.sqrPriceField ::text').extract_first().strip() if x1.css('div.right-contain div.sqrPrice >span.sqrPriceField ::text').extract_first() else ''
            
            self.dict_val={
                'unit_type':unit_type,
                'build_up_area':build_up_area,
                'status_details':final_dict,
                'description':description,
                'total_price':total_price,
                'price_per_sqft':price_per_sqft,
                'Price_range':response.css('div.secValueUp ::text').extract_first(),
                }
            
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
        for x in response.css('div.unitSlide >ul >li'):
            
            unit_type=''
            build=''
            unit_price=''
            unit_type=x.css('li >div.propDtls >div.bed ::text').extract_first()
            build=x.css('li >div.propDtls >div.space ::text').extract_first()
            unit_price='('+unit_type +'->'+build+')'
            update_list.append(unit_price)
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
        
        item={
             
             'units':units,
             'towers':towers,
             'unit_price':unit_price_final,
             
             'about_project':about_project,
             'table':col_final,
             'Project Status':status,
             # 'property_deatils':self.dict_val,
             'Super Built Area':self.dict_val['build_up_area'],
             'Price Range':self.dict_val['Price_range'],
             'Price Per Sq Ft':self.dict_val['price_per_sqft'],
             'Description':self.dict_val['description'],
             'Bedrooms':self.dict_val['unit_type'],
             'project_description':project_description,
             'project_highlights':project_highlights,
             'final_val_amn':final_val_amn,
             'rera_no':rera_no,
             'specification':response.css('div.projLBlock >div.constUpdate >div.consUpdateBlock >div.specContainer ::text').extract()

            }
        items.update(item)
        
        #self.item_list.append(items)
        #for values in self.item_list:
       
        #yield items
        
        yield scrapy.Request('http://www.magicbricks.com/propertyDetails/Project-Rates-Trends-Month?psmid='+items['id']+'&propType=10002&localityid=%s&localityName=%s'%(locality_id,self.name), callback=self.project_history,errback=self.errback_httpbin,meta={'items_val': items})
        #if item['about_project']:
            #yield scrapy.Request(items['about_project'],callback=self.about_project,errback=self.errback_httpbin,meta={'items_val': items})

    def project_history(self,response):
       
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