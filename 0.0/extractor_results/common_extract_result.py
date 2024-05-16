
import requests
from bs4 import BeautifulSoup
import json
import furl
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO) 

# This is the common function to extract result for all domain

def extract_result(html_content, input_url):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        input_url_hostname = urlparse(input_url).hostname
        # read select json file 
        result = []
        with open('select_json_file.json','r') as file:
            json_data = json.load(file)
            for item in json_data:
                authority = item.get('authority','')
                if authority in input_url_hostname:
                    
                    # Wayfair
                    if 'www.wayfair.com' in input_url:
                        tag = item["title_selector"]["tag"]
                        class_ = item["title_selector"]["class"]
                        product_title = soup.find(tag, class_)
                        if product_title:
                            title = product_title.text.strip()
                        else:
                            title = None
   
                        brand_class = item["brand"]["class"]
                        product_brand = soup.find(class_=brand_class)

                        if product_brand:
                            brand = product_brand.a.text.strip()
                        else:
                            brand = None

                    # Walmart
                    # elif 'www.walmart.com' in input_url:

                    #     "Extract Product Title"
                    #     tag = item["title_selector"]["tag"]
                    #     class_ = item["title_selector"]["class"]
                    #     product_title = soup.find(tag, class_)
                    #     if product_title:
                    #         title = product_title.text.strip()
                    #     else:
                    #         title = None
                        
                    #     brand_class = item["brand"]["class"]
                    #     product_brand = soup.find(class_=brand_class)

                    #     if product_brand:
                    #         brand = product_brand.text.strip()
                    #     else:
                    #         brand = None

                    # Macys
                    # elif 'www.macys.com' in input_url:
                    #     tag = item["title_selector"]["tag"]
                    #     class_ = item["title_selector"]["class"]
                    #     product_title = soup.find(tag, class_)
                    #     if product_title:
                    #         title = product_title.text.strip()
                    #     else:
                    #         title = None

                    #     brand_tag = item["brand"]["tag"]
                    #     brand_class = item["brand"]["class"]
                    #     product_brand = soup.find(brand_tag,class_=brand_class)
                    #     if product_brand:
                    #         brand = product_brand.text.strip()
                    #     else:
                    #         brand = None
                        
                    # Adidas
                    # elif 'www.adidas.com' in input_url:
                        # class_ = item["title_selector"]["class"]
                        # product_title = soup.find(class_=class_)
                        # if product_title:
                        #     title = product_title.text.strip()
                        # else:
                        #     title = None
                        
                        # brand_tag = item["brand"]["tag"]
                        # if brand_tag == "null":
                        #     brand = None
                        # else:
                        #     brand = None

                    # # Kohls
                    # elif 'www.kohls.com' in input_url:
                    #     class_ = item["title_selector"]["class"]
                    #     product_title = soup.find(class_=class_)
                    #     if product_title:
                    #         title = product_title.text.strip()
                    #     else:
                    #         title = None
                        
                    #     brand_class = item["brand"]["class"]
                    #     product_brand = soup.find(class_=brand_class)
                    #     if product_brand:
                    #         brand = product_brand.a.text.strip()
                    #     else:
                    #         brand = None
                    
                    # Nike       
                    # elif 'www.nike.com' in input_url:
                    #     tag = item["title_selector"]["tag"]
                    #     class_ = item["title_selector"]["class"]
                    #     product_title = soup.find(tag,id=class_)
                    #     if product_title:
                    #         title = product_title.text.strip()
                    #     else:
                    #         title = None


                    # awaytravels
                    # elif 'www.awaytravel.com' in input_url:
                    #     title_selector = item.get("title_selector")
                    #     if title_selector:
                    #         tag = title_selector.get("tag")
                    #         class_ = title_selector.get("class")
                    #         if tag and class_:
                    #             product_title = soup.find(tag, class_=class_)
                    #             if product_title and product_title.find('h1'):
                    #                 title = product_title.find('h1').text.strip()
                    #             else:
                    #                 title = None
                    #         else:
                    #             title = None
                    #     else:
                    #         title = None


                    # awaytravel
                    elif 'www.awaytravel.com' in input_url:
                        tag = item["title_selector"]["tag"]
                        class_ = item["title_selector"]["class"]
                        product_title = soup.find(tag,class_=class_)
                        if product_title:
                            title = product_title.h1.text.strip()
                        else:
                            title = None
            
                        brand_class = item["brand"]["class"]
                        brand_tag = item["brand"]["tag"]
                        product_brand = soup.find()
                        if product_brand:
                            brand = product_brand.a.text.strip()
                        else:
                            brand = None


                    # nike
                    elif 'www.nike.com' in input_url:
                        tag = item["title_selector"]["tag"]
                        class_ = item["title_selector"]["class"]
                        product_title = soup.find(tag,id=class_)
                        if product_title:
                            title = product_title.text.strip()
                        else:
                            title = None
            
                        brand_class = item["brand"]["class"]
                        brand_tag = item["brand"]["tag"]
                        product_brand = soup.find(brand_tag, id=brand_class)
                        print(product_brand)
                        if product_brand:
                            brand = product_brand.text.strip()
                        else:
                            brand = None

                     # ulta
                    elif 'www.ulta.com' in input_url:
                        tag = item["title_selector"]["tag"]
                        class_ = item["title_selector"]["class"]
                        product_title = soup.find(tag,class_=class_)
                        if product_title:
                            title = product_title.text.strip()
                        else:
                            title = None
            
                        brand_tag = item["brand"]["tag"]
                        brand_class = item["brand"]["class"]
                        product_brand = soup.find(brand_tag, class_=brand_class)
                        if product_brand:
                            brand = product_brand.a.text.strip()
                        else:
                            brand = None
                    
                    # anovaculinary
                    elif 'anovaculinary.com' in input_url:
                        tag = item["title_selector"]["tag"]
                        class_ = item["title_selector"]["class"]
                        product_title = soup.find(tag,id=class_)
                        if product_title:
                            title = product_title.text.strip()
                        else:
                            title = None
            
                        brand_class = item["brand"]["class"]
                        product_brand = soup.find(class_=brand_class)
                        if product_brand:
                            brand = product_brand.text.strip()
                        else:
                            brand = None


                    # dickssportinggoods
                    elif 'www.dickssportinggoods.com' in input_url:
                        tag = item["title_selector"]["tag"]
                        class_ = item["title_selector"]["class"]
                        product_title = soup.find(tag,class_=class_)
                        print(product_title)
                        if product_title:
                            title = product_title.text.strip()
                        else:
                            title = None
            
                        brand_class = item["brand"]["class"]
                        brand_tag = item["brand"]["class"]
                        # product_brand = soup.find(brand_tag, itemprop=brand_class)
                        product_brand = soup.find(brand_tag, itemprop="brand")
                        if product_brand:
                            brand = product_brand.text.strip()
                        else:
                            brand = None
                    



                    # Extract title and brand from select_json_file
                    data_store = {
                        'title': title,
                        'brand': brand,
                        'url': input_url
                    }
                    result.append(data_store)

            return result
        
    except Exception as e:
        logging.error("An error occurred while extracting results: %s", e)
        return None
