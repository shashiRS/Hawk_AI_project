# -*- coding: utf-8 -*-
import scrapy
import pdb
import itertools

class CommonFloorDataSpider(scrapy.Spider):
    name = 'common_floor_data'
    allowed_domains = ['commonfloor.com']
    #start_urls = ['http://commonfloor.com/']

    def __init__(self, *args, **kwargs):
        self.start_url=[]
        self.item_list=[]
        self.item_list2=[]
        self.projct_overview={}
        j=0
        self.area_id=["24456",
"42838",
"3877",
"36011",
"32685",
"41107",
"38317",
"46249",
"36262",
"46309",
"3886",
"3888",
"6530",
"3889",
"35262",
"46006",
"29832",
"3897",
"3902",
"24455",
"39472",
"37356",
"44289",
"3913",
"46951",
"39592",
"45930",
"4593",
"45221",
"3916",
"3924",
"23697",
"3927",
"44585",
"46596",
"46260",
"36166",
"3934",
"45213",
"25746",
"5941",
"36263",
"27375",
"45823",
"30486",
"41477",
"3942",
"31042",
"44487",
"33148",
"37388",
"3950",
"35987",
"46337",
"45962",
"3957",
"5239",
"29633",
"5535",
"45919",
"3960",
"3962",
"5471",
"44604",
"25076",
"32404",
"46475",
"36264",
"46667",
"3973",
"3975",
"3978",
"42452",
"3981",
"3983",
"3985",
"35861",
"3988",
"3991",
"3997",
"44644",
"3998",
"41198",
"4001",
"4002",
"41636",
"44863",
"4007",
"4010",
"4011",
"5383",
"45918",
"46136",
"36005",
"42842",
"41666",
"41673",
"29554",
"4020",
"4021",
"4022",
"30854",
"25338",
"4026",
"4027",
"4034",
"4031",
"4036",
"41736",
"4041",
"46595",
"33067",
"45305",
"31044",
"46013",
"35736",
"4048",
"4051",
"4052",
"31506",
"25783",
"4057",
"25394",
"35982",
"4065",
"5938",
"4066",
"46822",
"4068",
"4069",
"4070",
"36658",
"4072",
"45123",
"41476",
"25743",
"46358",
"46590",
"4076",
"46246",
"39591",
"45951",
"25722",
"37473",
"4083",
"46657",
"4084",
"45242",
"46227",
"27412",
"4085",
"5385",
"36010",
"27364",
"4087",
"4089",
"45756",
"4078",
"4097",
"42849",
"33035",
"4101",
"4102",
"46044",
"46319",
"4103",
"4106",
"30240",
"46254",
"4112",
"4113",
"6240",
"45950",
"5538",
"45210",
"42304",
"4121",
"4126",
"46664",
"6343",
"4127",
"42552",
"4132",
"29552",
"44168",
"33480",
"36032",
"42453",
"35851",
"4138",
"31158",
"4139",
"30585",
"4141",
"46630",
"4142",
"45429",
"4146",
"35983",
"4147",
"36004",
"4150",
"41665",
"43042",
"4152",
"4153",
"4159",
"35784",
"31973",
"4160",
"44582",
"4161",
"30951",
"4165",
"4651",
"4168",
"4170",
"4172",
"29596",
"45925",
"4173",
"31159",
"35852",
"37170",
"36673",
"39937",
"46363",
"4177",
"46493",
"40464",
"37397",
"44765",
"29607",
"5411",
"4186",
"30785",
"30498",
"35850",
"4190",
"42721",
"46228",
"4196",
"44688",
"45289",
"46030",
"4609",
"45958",
"35753",
"33324",
"5382",
"46209",
"23695",
"45037",
"5386",
"25639",
"24880",
"4208",
"42306",
"46580",
"29331",
"45294",
"4213",
"38081",
"4214",
"36390",
"30997",
"4216",
"46054",
"31376",
"4217",
"4220",
"5537",
"35988",
"4224",
"45438",
"41168",
"45328",
"36388",
"32337",
"46824",
"4235",
"4237",
"4238",
"4239",
"4240",
"36003",
"37015",
"4241",
"4242",
"4245",
"45771",
"4607",
"4246",
"31839",
"24682",
"4250",
"4251",
"4254",
"31093",
"36911",
"46312",
"32805",
"46310",
"32655",
"36253",
"41165",
"4269",
"30720",
"4273",
"32184",
"25519",
"30692",
"46414",
"45635",
"39473",
"46703",
"4290",
"5223",
"4630",
"4296",
"45496",
"4294",
"46751",
"41438",
"45442",
"43088",
"43333",
"36577",
"4299",
"39148",
"4516",
"4300",
"35853",
"46183",
"45238",
"31025",
"31922",
"46125",
"4306",
"31285",
"32202",
"4312",
"4650",
"46118",
"42752",
"46073",
"4315",
"4318",
"37607"]
        self.localit=["A S Rao Nagar",
"Abdullapurmet",
"Abids",
"Adarsh Nagar",
"Adibatla",
"Adikmet",
"Afzal Gunj",
"Ahmedguda",
"Almasguda",
"Alugaddabavi",
"Alwal",
"Amberpet",
"Ameenpur",
"Ameerpet",
"Anandbagh",
"Annojiguda",
"Appa Junction",
"Attapur",
"Bachupally",
"Badangpet",
"Bahadurpally",
"Bahadurpura",
"Bairagiguda",
"Bala Nagar",
"Balamrai",
"Balapur",
"Balkampet",
"Bandlaguda",
"Bandlaguda - Nagole",
"Banjara Hills",
"Basheerbagh",
"Beeramguda",
"Begumpet",
"Bhanur",
"Bharat Heavy Electricals Limited",
"Bhavani Nagar",
"Bhogaram",
"Bhoiguda",
"Bhongir",
"Bhuvanagiri",
"Bibinagar",
"BN Reddy Nagar",
"Boduppal",
"Bogaram",
"Bolaram",
"Borabanda",
"Bowenpally",
"Bowrampet",
"Budvel",
"Burgul",
"Champapet",
"Chanda Nagar",
"Chandrayanagutta",
"Chandupatla",
"Chengicherla",
"Cherlapally",
"Chevalla",
"Chikkadapally",
"Chilkur",
"Chinnamangalaram",
"Chintal",
"Chintalkunta",
"Chintapallyguda",
"Chowdhariguda",
"Dammaiguda",
"Dasarlapally",
"Dattatreya Nagar",
"Dayara",
"Deshmuki Village",
"Dhoolpet",
"Dilsukhnagar",
"Domalguda",
"Dullapally",
"Dundigal",
"East Marredpally",
"ECIL",
"Edulanagulapalle",
"Erragadda",
"Falaknuma",
"Film Nagar",
"Financial District",
"Gachibowli",
"Gagillapur",
"Gajularamaram",
"Gandhi Nagar",
"Gandi Maisamma",
"Gandipet",
"Ghansi Bazar",
"Ghatkesar",
"Golkonda",
"Gopanpally",
"Gowdavalli",
"Gowlipura",
"Gudimalkapur",
"Gulshan-e-Iqbal Colony",
"Gundlapochampally",
"Gunrock Enclave",
"Gurram Guda",
"Habsiguda",
"Hafeezpet",
"Hakimpet",
"Hanuman Nagar Colony",
"Hasmathpet",
"Hastinapuram",
"Hayat Nagar",
"Hi Tech City",
"Himayath Nagar",
"Humayun Nagar",
"Hyder Nagar",
"Hyderguda",
"Ibrahim Bagh",
"Ibrahimpatnam",
"Indresham",
"Isnapur",
"Jahanuma",
"Jalpally",
"Jam Bagh",
"Jawahar Nagar",
"Jeedimetla",
"Jeera",
"Jubilee Hills",
"Kachiguda",
"Kakaguda",
"Kalasiguda",
"Kanchan Bagh",
"Kandukur",
"Kapra",
"Kardhanur",
"Karkhana",
"Karmanghat",
"Karwan",
"Katedan",
"Kavadiguda",
"Kavuri Hills",
"Kazipally",
"Keesara",
"Keesara-Yadagirigutta Road",
"keshampet",
"Khairatabad",
"Kings Colony",
"Kismatpur",
"Koheda",
"Kokapet",
"Kollur",
"Kompally",
"Kondakal",
"Kondapur",
"Kongara Kalan",
"Korremula",
"Kothaguda",
"Kothapet",
"Kothur",
"Koti",
"Kowkur",
"KPHB",
"Kukatpally",
"Kurmaguda",
"Kushaiguda",
"Lakdi Ka Pul",
"Lal Darwaza",
"Lalapet",
"Lallaguda",
"Langar Houz",
"Laxma Reddy Palem Colony",
"Laxmiguda",
"LB Nagar",
"Lingampally",
"Lothkunta",
"M Turkapally",
"Madhapur",
"Madhura Nagar",
"Madinaguda",
"Mahadevpur Colony",
"Maheshwaram",
"Maisireddipalle",
"Majarguda",
"Malakpet",
"Malkajgiri",
"Malkaram",
"Mallampet",
"Mallapur",
"Manchirevula",
"Manikonda",
"Manneguda",
"Mansoorabad",
"Maruti Nagar",
"Masab Tank",
"Mazidpur",
"Medak Road",
"Medchal",
"Medipalli",
"Meerpet",
"Mehadipatnam",
"Mehdipatnam",
"Mettakanigudem",
"Mettuguda",
"Mirkhanpet",
"Miyapur",
"Moghalpura",
"Moinabad",
"Mokila",
"Moosapet",
"Moosarambagh",
"Moti Ganpur",
"Moti Nagar",
"Moula Ali",
"Musheerabad",
"Muthangi",
"Mylargada",
"Nacharam",
"Nadergul",
"Nagaram",
"Nagarjuna Sagar Road",
"Nagole",
"Nallagandla",
"Nallakunta",
"Nampally",
"Nanakramguda",
"Nandigama",
"Narapally",
"Narayanguda",
"Narketpalli",
"Narsapur",
"Narsingi",
"Nawab Saheb Kunta",
"Neeladri Nagar",
"Neknampur",
"Neredmet",
"New Bowenpally",
"New Malakpet",
"New Mallepally",
"New Nallakunta",
"Nizampet",
"Nizampet Road",
"NTR Nagar",
"Old Bowenpally",
"Osman Nagar",
"Osman Sagar Road",
"Padma Rao Nagar",
"Pahadi Shareef",
"Pashamylaram",
"Patancheru",
"Patancheru-Shankarpalli Road",
"Patighanpur",
"Pedda Amberpet",
"Peerancheru",
"Peerlagudam",
"Peerzadiguda",
"Pochampally",
"Pocharam",
"Polkampally",
"Pragathi Nagar",
"Prashanth Nagar",
"Pulimamidi",
"Punjagutta",
"Puppalaguda",
"Quthbullapur",
"Qutub Shahi Tombs",
"Ragannaguda",
"Rai Durg",
"Raikal",
"Raj Bhavan Road",
"Rajeev Nagar",
"Rajendra Nagar",
"Ram Nagar",
"Ramakrishnapuram",
"Ramanthapur",
"Ramayampet",
"Ramchandra Puram",
"Ramgopalpet",
"Ramoji Film City",
"Rampally",
"Rani Gunj",
"Rasoolpura",
"Ravulapalle Khurd",
"Rendlagadda",
"Riyasat Nagar",
"Rudraram",
"S D Road",
"Sadashivpet",
"Saidabad",
"Saifabad",
"Sainikpuri",
"Saleem Nagar",
"Sanath Nagar",
"Sangareddy",
"Sanjeeva Reddy Nagar",
"Santosh Nagar",
"Saroor Nagar",
"Secunderabad",
"Seetharampally",
"Serilingampally",
"Shadnagar",
"Shahbaad",
"Shaikpet",
"Shamirpet",
"Shamshabad",
"Shankarpalli",
"Shanthi Nagar",
"Sheriguda",
"Shivaji Nagar",
"Siddhartha Nagar",
"Sikh Village",
"Sindhi Colony",
"Sitaphalmandi",
"Sivarampalli",
"Somajiguda",
"Sri Nagar Colony",
"Srinagar Colony",
"Srisailam Highway",
"Subhash Nagar",
"Suchitra Road",
"Sultanpalle",
"Sultanpur",
"Suraram",
"Tallaguda",
"Tarnaka",
"Tellapur",
"Thimmapur",
"Toli Chowki",
"Toroor",
"Trimulgherry",
"Tukaram Gate",
"Tukkuguda",
"Tulekhurd",
"Tupran",
"Turkayamjal",
"Uppaguda",
"Uppal",
"Upparpally",
"Upperpally",
"Vanasthalipuram",
"Vattepally",
"Vattinagulapally",
"Velimela",
"Venkat Reddy Colony",
"Venkatapuram",
"Vijay Nagar colony",
"Vijayawada Highway",
"Walker Town",
"Warangal highway",
"West Marredpally",
"Whitefields",
"Yadagirigutta",
"Yakhutpura",
"Yamnampet",
"Yapral",
"Yousufguda",
"Zahirabad"]
        

        for i in range(1,5):
            for id,loc in itertools.izip(self.area_id,self.localit):
                url='https://www.commonfloor.com/project-search?city=Hyderabad&search_intent=sale&house_type[]=Apartment&house_type[]=Builder Floor&house_type[]=Villa&property_location_filter[]=area_%s&prop_name[]=%s&polygon=1&page=%s&page_size=30'%(id,loc,i)
                #url='https://www.commonfloor.com/project-search?city=Bangalore&search_intent=sale&property_location_filter[]=area_%s&prop_name[]=%s&polygon=1&page=%s&page_size=30'%(self.id_loc,self.name,i)
                self.start_url.append(url)
               
      
        
        super(CommonFloorDataSpider, self).__init__(*args, **kwargs)




    def start_requests(self):
       
        for url in self.start_url:
            yield scrapy.Request(url,callback=self.parse_details,dont_filter=True)
            
    def parse_details(self, response):
        item={}
        link_list=[]
        for d1 in response.css('div.snb-projecttile'):
            title=''
           
            
            project_by=''
            link=''
            for item in d1.css('a.snb-projecttile-ab >h2 ::text').extract():
                title+=item
            for item in d1.css('a.snb-projecttile-ab >h4 ::text').extract():
                project_by+=item
            link=response.urljoin(d1.css('a.snb-projecttile-ab ::attr(href)').extract_first())    
            
            
            
            
            item={
                'project_name':title,
                
                'project_by':project_by,
                'link':link
                }
            link_list.append(item)
            
            
        if link_list:
            for item_link in link_list:
                yield scrapy.Request(item_link['link'],callback=self.fetch_detail,meta={'items_val': item_link})  
            
            
    def fetch_detail(self,response):
        
        items = response.meta.get('items_val')
        item=[]
        launched=''
        status=''
        possesion=''
        features_list=[]
        project_overview=[]
        project_description=''
        location_tab=''
        rera_no=''
        header=[]
        col_final=[]
        for val in response.css('div#project-overview-details'):
            #if len(val.css('div.titlelist >div.datatitle >span::text').extract())>1:
                
            launched=val.css('div.titlelist >div.datatitle >span::text').extract_first()
            for x in val.css('div.titlelist >div.datatitle >div >div::text').extract():
                 possesion+=x
            status=val.css('div.titlelist >div.datalist >span.prolist::text').extract_first()
            
            for item in val.css('div.pdltnone'):
                project_over_view_key=''
                project_over_view_value=''
                
                for x1 in item.css('div.datatitle ::text').extract():
                      project_over_view_key+=x1
                for x2 in item.css('div.datalist ::text').extract():
                    project_over_view_value+=x2
                z={}
                z={project_over_view_key.strip(): project_over_view_value.strip(),
                                  }
                self.projct_overview.update(z)  
                #project_overview.append(projct_overview)
                
        header=response.css('div#house-details >div > div.header >div.col ::text').extract() 
        col=[]
        for x1 in response.css('div#house-details >div > div.body'):
            col_list=[]
            for x2 in x1.css('div.col'):
                
                col_val=""
                for val1 in x2.css('div.col ::text').extract():
                    
                    col_val+=val1
                
                col_list.append(col_val)
            col.append(col_list)  
        
        for x3 in col:
            col_semi=[]
            final_dict={}
            for i in range(0,len(x3)):
                z={}
                z={header[i]:x3[i]}
                final_dict.update(z)
                #col_semi.append(final_dict)
            col_final.append(final_dict)    
            
        for x1 in response.css('div.colds >span::text').extract():
            rera_no+=x1
        
        amenities_list=[]
        amenities_dict={}
        for x2 in response.css('div#amenities >div >div.row >div.contenttext >div.amtlist >ul'):
            amenities_key=''
            amenities_value=''
            
            for y in x2.css('li >span::text').extract():
                amenities_key+=y
            for y in x2.css('li::text').extract():
                amenities_value+=y  
            z={}
            z={amenities_key.strip():amenities_value.strip()
                            }
            amenities_dict.update(z)
            #amenities_list.append(amenities_dict)
        
        project_specification=""
        for x in response.css('div#amenities >div >div.row >div >div.contenttext >div.textshowhide ::text').extract():
            project_specification+=x
        address=''
        about_builder=''
        for x in response.css('div#about-project-builder >div >div >div >div >p.add::text').extract():
            address+=x
        for x in response.css('div#about-project-builder >div >div >div >div >div.textshowhide ::text').extract():
            about_builder+=x
      
        about_project=''
        for x in response.css('div#about >div >div.contenttext >div.textshowhide::text').extract():
            about_project+=x
        item={
            'launched':launched,
            
            'Project status':status,
            'possesion':possesion,
            'location':self.projct_overview['Location'],
            'table_data':col_final,
            'Price':final_dict['Price'],
            'Build_Up_Area':final_dict['Super Built-Up Area'],
            'Unit_Types':final_dict['Unit Types'],
            'rera_no':rera_no,
            'amenities_list':amenities_dict,
            'project_specification':project_specification,
            'about_builder':about_builder,
            'address':address,
            'about_project':about_project
            #'location_tab':location_tab,
            }      
        items.update(item) 
        yield items
     
     
   