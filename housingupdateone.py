# from housing.items import HousingItemBuy
from scrapy import Spider
from scrapy.http.request import Request

#To parse the JSON received
import json
import pdb
from scrapy import Item, Field

class HousingItemBuy(Item):
    ad_id = Field()
    title = Field()
    price = Field()
    area = Field()
    url = Field()
    date_added = Field()
    coordinates = Field()
    number_of_bedrooms = Field()
    number_of_toilets = Field()
    gas_pipeline = Field()
    lift = Field()
    parking = Field()                                   
    gym = Field()
    swimming_pool = Field()
    city = Field()
    locality = Field()
    micro_locality = Field()
    contact_persons_name = Field()
    contact_persons_number = Field()
    contact_persons_id = Field()
    profile_uuid = Field()
    per_sqft_rate = Field()
    apartment_type = Field()
    facing = Field()
    # formatted_price = Field()
    property_type = Field()
    status = Field()
    street_info = Field()
    show_loan_option = Field()

class HousingSpider(Spider):
    name = "housing"
    allowed_domains = ["housing.com"]
    # custom_settings = {'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}
    

    def start_requests(self):
        #We have 1080 pages to fetch
        for count in range(1,173):
            
            print "Getting page : %s" %count
            
            yield Request("https://buy.housing.com/api/v4/buy/index/filter?poly=747be13fe47cb8ae14c3&results_per_page=30&p=" + str(count) + "&total=115&np_total_count=57", self.parse_buy)

           
    def parse_buy(self, response):
        pdb.set_trace()
        
        #Since the response is purely JSON
        text =  response.body

        #Parsing it using the builtin json utility
        parsed_json = json.loads(text)
        # data_obj = json.loads(data)
        #For each entry, we will store all the information we defined earlier in items.py
        #The parsed json can be read as a dict. Examining the JSON, we can easily navigate 
        #to where we have the data we need.

        for iter in range(30):
            item = HousingItemBuy()
            pdb.set_trace()
            try:
                item['per_sqft_rate'] = parsed_json["hits"][iter]["inventory_configs"][0]["per_sqft_rate"]
                item['apartment_type'] = parsed_json["hits"][iter]["inventory_configs"][0]["apartment_type"]
                item['number_of_toilets'] = parsed_json["hits"][iter]["inventory_configs"][0]["number_of_toilets"]
                item['number_of_bedrooms'] =parsed_json["hits"][iter]["inventory_configs"][0]["number_of_bedrooms"]
                item['facing'] = parsed_json["hits"][iter]["inventory_configs"][0]["facing"]
                item['price'] = parsed_json["hits"][iter]["inventory_configs"][0]["formatted_price"]
                item['property_type'] = parsed_json["hits"][iter]["inventory_configs"][0]["property_type"]
                # item['available_from'] = parsed_json["hits"][iter]
                item['city'] = parsed_json["hits"][iter]["polygons_hash"]["city"]["name"]
                item['locality'] = parsed_json["hits"][iter]["polygons_hash"]["locality"]["name"]
                item['micro_locality'] = parsed_json["hits"][iter]["polygons_hash"]["sublocality"]["name"]
                item['status'] = parsed_json["hits"][iter]["status"]
                item['street_info'] = parsed_json["hits"][iter]["street_info"]
                item['show_loan_option'] = parsed_json["hits"][iter]["show_loan_option"]
                item['url'] = parsed_json["hits"][iter]["inventory_canonical_url"]
                item['title'] = parsed_json["hits"][iter]["title"]
                item['coordinates'] = parsed_json["hits"][iter]["location_coordinates"]
                item['date_added'] = parsed_json["hits"][iter]["date_added"]
                item['area'] = parsed_json["hits"][iter]["inventory_configs"][0]["area"]
                item['profile_uuid'] = parsed_json["hits"][iter]["contact_persons_info"][0]["profile_uuid"]
                # item['ad_contact_persons_number'] = parsed_json["hits"][iter]["contact_persons_info"][0]["contact_no"]
                item['contact_persons_id'] = parsed_json["hits"][iter]["contact_persons_info"][0]["contact_person_id"]
                item['contact_persons_name'] = parsed_json["hits"][iter]["contact_persons_info"][0]["name"]
                
                #Some entries do not have the ad_city/ad_locality variable. 
                # try:
                #     item['ad_city'] = parsed_json["hits"][iter]["display_city"][0]
                # except :
                #     item['ad_city'] = "None given"
                    
                # try:
                #     item['ad_locality'] = parsed_json["hits"][iter]["display_city"][1]
                # except :
                #     item['ad_locality'] = "None given"
                    
                item['gas_pipeline'] = parsed_json["hits"][iter]["inventory_amenities"]["has_gas_pipeline"]
                item['lift'] = parsed_json["hits"][iter]["inventory_amenities"]["has_lift"]
                item['parking'] = parsed_json["hits"][iter]["inventory_amenities"]["has_parking"]
                item['gym'] = parsed_json["hits"][iter]["inventory_amenities"]["has_gym"]
                item['swimming_pool'] = parsed_json["hits"][iter]["inventory_amenities"]["has_swimming_pool"]
                item['ad_id'] = parsed_json["hits"][iter]["id"]
            except:
                pass
            yield item