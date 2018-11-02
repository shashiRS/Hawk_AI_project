# -*- coding: utf-8 -*-
import scrapy
import pdb
from scrapy_splash import SplashRequest

class SulekhadataSpider(scrapy.Spider):
    name = 'sulekhadata'
    allowed_domains = ['sulekha.com']
    def __init__(self, name=None, *args, **kwargs):
        self.start_url=[]
        self.result_url=[]
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
        
        for loc in self.localit:
            for i in range(1,11):
            # url2='https://www.99acres.com/search/project/buy/residential/hebbal-bangalore?search_type=QS&search_location=CP20&lstAcn=CP_R&lstAcnId=20&src=CLUSTER&preference=S&selected_tab=3&city=20&res_com=R&isvoicesearch=N&keyword=sahakar %20nagar%20bangalore&np_search_type=R2M%2CNL%2CNP&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null'
                url='http://property.sulekha.com/ProjectAd/LoadListingsAjax2017?parameters=&url=%2Fnew-projects-in-'+loc+'-bangalore-for-sale_page-'+str(i)+'&FetchCount=0&callFrom=&listingsCount=0&NextAdId='
                self.start_url.append(url)
            super(SulekhadataSpider, self).__init__(*args, **kwargs)


    def start_requests(self):
        for url in self.start_url:
            yield SplashRequest(url, self.parseurl)

  
    def parseurl(self,response):
        for i in response.css('li.project-list.card.left >div.listing-detail >div >h3 >a'):
            for inner in i.css('::attr(href)').extract():
               
                urla='http://property.sulekha.com'+inner
                yield scrapy.Request(urla, self.parse)
        

    def parse(self,response):
        pdb.set_trace()
        item={
        'Project_name':response.css('div.cover-details >div.banner-group >h1 ::text').extract(),
        'location':response.css('div.cover-details >div.banner-group >strong ::text').extract(),
        'Landmark':response.css('div.cover-details >div.banner-group >span ::text').extract(),
        'Possession:':response.css('div.config >div.date ::text')[2].extract(),
        'Base Price':response.css('div.config >div.base >b ::text').extract(),
        'Property Type':response.css('div.config >div.pro-type ::text')[2].extract(),
        'BHK Type':response.css('div.config >div.pro-type ::text')[5].extract(),
        'Area':response.css('div.config >div.pro-area ::text')[3].extract(),
        'Posted':response.css('div.posted ::text').extract(),
        'Project_Overview':response.css('div.poster.overview.card ::text').extract(),
        'Project_description':response.css('div#description >p ::text').extract(),
        'Price Information & Trends':response.css('div.item.value ::text').extract(),

        }
        yield item