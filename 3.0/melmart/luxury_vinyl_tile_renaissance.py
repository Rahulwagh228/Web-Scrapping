import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'melmart_vinyl_renaissance.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)


cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'ffvisitorids': '{"melmart":"4d652bf68c114b209333b19e79e05b46"}',
    'ffvendorids': '{"melmart":"bafa231287eb484dabfa8648c68d4692"}',
    '_ga': 'GA1.2.1471538261.1715146434',
    '_gid': 'GA1.2.11735546.1715146434',
    '__stripe_mid': 'dbf45703-7c27-4e74-bccc-c850781e7c987eee8f',
    'sbjs_udata': 'vst%3D4%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36',
    'woocommerce_products_per_page': '48',
    'sbjs_session': 'pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fcapstone-tile-12-x-24-calacatta-cream-mel6521-6%2F',
    '_ga_BPEVSBVR9J': 'GS1.2.1715160486.4.1.1715162481.0.0.0',
    '__stripe_sid': '504af3e8-6918-4866-a4b9-2d4f846f45a2b3e0e1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; ffvisitorids={"melmart":"4d652bf68c114b209333b19e79e05b46"}; ffvendorids={"melmart":"bafa231287eb484dabfa8648c68d4692"}; _ga=GA1.2.1471538261.1715146434; _gid=GA1.2.11735546.1715146434; __stripe_mid=dbf45703-7c27-4e74-bccc-c850781e7c987eee8f; sbjs_udata=vst%3D4%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36; woocommerce_products_per_page=48; sbjs_session=pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fcapstone-tile-12-x-24-calacatta-cream-mel6521-6%2F; _ga_BPEVSBVR9J=GS1.2.1715160486.4.1.1715162481.0.0.0; __stripe_sid=504af3e8-6918-4866-a4b9-2d4f846f45a2b3e0e1',
    'origin': 'https://melmart.com',
    'priority': 'u=0, i',
    'referer': 'https://melmart.com/brands/renaissance/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

data1 = {
    'ppp': '48',
}


def get_urls(url):
    response = requests.get(url, cookies=cookies, headers=headers, data=data1)
    # print(response.status_code)
    soup = BeautifulSoup(response.content,'html.parser')
    data = []

# a.woocommerce-LoopProduct-link - class by web scrapper
    for link in soup.find_all(class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
        url = link.get('href')
        data.append(url)
    return data


def get_product_data(url):
 
    response = requests.get(url, cookies=cookies, headers=headers)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")

    d={}
    title = soup.find('h2', class_='size-h2 color-primary product-brand').text.strip()
    # print(title)
    d['title'] = title

    brand = soup.find('h1', class_='product_title entry-title color-body weight-bold text-uppercase family-body').text.strip()
    d['brand'] =  brand


    specs = {}

    specification = soup.find('table', class_='shop_attributes').find_all('tr')
        # print(specification)
    for item in specification:
            key = item.find('th', class_='product-attribute').text.strip()
            value = item.find('td').text.strip()
            specs.update({key:value})


    for i in  ['Bevel', 'Collection', 'Edge', 'Floor Type', 'Installation', 'Length', 'Plank Width', 'Radiant Heat', 'Thickness', 'Wear Layer', 'Packaging', 'Warranty', 'Sustainability']:
         if i not in specs:
              specs[i] = ' '
    

    d['Bevel'] = specs['Bevel']
    d['Collection'] = specs['Collection']
    d['Edge'] = specs['Edge']
    d['Floor Type'] = specs['Floor Type']
    d['Installation'] = specs['Installation']
    d['Length'] = specs['Length']
    d['Plank Width'] = specs['Plank Width']
    d['Radiant Heat'] = specs['Radiant Heat']
    d['Thickness'] = specs['Thickness']
    d['Wear Layer'] = specs['Wear Layer']
    d['Packaging'] = specs['Packaging']
    d['Warranty'] = specs['Warranty']
    d['Sustainability'] = specs['Sustainability']


    img = soup.select('.tpwpg-thumbnail img')
    # print(img)
    for i in img:
        alt = i['alt']
        src = i['src']
        d['image_name'] = alt
        d['images'] = src


        Load_csv(d)
# ---------------------------------------------------------------

collections = {
     '0':'https://melmart.com/brands/renaissance/',
     '1':'https://melmart.com/brands/renaissance/page/2/',
     '2':'https://melmart.com/brands/renaissance/page/3/',
     '3':'https://melmart.com/brands/renaissance/page/4/',
     '4':'https://melmart.com/brands/renaissance/page/5/',
     '5':'https://melmart.com/brands/renaissance/page/6/',
     '6':'https://melmart.com/brands/renaissance/page/7/',
     '7':'https://melmart.com/brands/renaissance/page/8/',
    #  '2':'',
   
}

for collection, url in collections.items():
  for u in get_urls(url):
    # print(u)
    get_product_data(u)


