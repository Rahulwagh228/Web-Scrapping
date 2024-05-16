import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'melmart_hardwood_savannah.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)


cookies = {
    'ffvisitorids': '{"melmart":"4d652bf68c114b209333b19e79e05b46"}',
    'ffvendorids': '{"melmart":"bafa231287eb484dabfa8648c68d4692"}',
    '_ga': 'GA1.2.1471538261.1715146434',
    '_gid': 'GA1.2.11735546.1715146434',
    '__stripe_mid': 'dbf45703-7c27-4e74-bccc-c850781e7c987eee8f',
    'woocommerce_products_per_page': '12',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-05-08%2013%3A26%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fcapstone-tile-12-x-24-calacatta-cream-mel6521-6%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelmart.com%2Fbrands%2Frenaissance%2F',
    'sbjs_first_add': 'fd%3D2024-05-08%2013%3A26%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fcapstone-tile-12-x-24-calacatta-cream-mel6521-6%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelmart.com%2Fbrands%2Frenaissance%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36',
    '__stripe_sid': '2c224092-5a26-401c-8e70-5a158646621395b8e5',
    'sbjs_session': 'pgs%3D53%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%3Fiso_floor_type%3Dhardwood',
    '_ga_BPEVSBVR9J': 'GS1.2.1715176611.5.1.1715178696.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'ffvisitorids={"melmart":"4d652bf68c114b209333b19e79e05b46"}; ffvendorids={"melmart":"bafa231287eb484dabfa8648c68d4692"}; _ga=GA1.2.1471538261.1715146434; _gid=GA1.2.11735546.1715146434; __stripe_mid=dbf45703-7c27-4e74-bccc-c850781e7c987eee8f; woocommerce_products_per_page=12; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-08%2013%3A26%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fcapstone-tile-12-x-24-calacatta-cream-mel6521-6%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelmart.com%2Fbrands%2Frenaissance%2F; sbjs_first_add=fd%3D2024-05-08%2013%3A26%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fcapstone-tile-12-x-24-calacatta-cream-mel6521-6%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fmelmart.com%2Fbrands%2Frenaissance%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36; __stripe_sid=2c224092-5a26-401c-8e70-5a158646621395b8e5; sbjs_session=pgs%3D53%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%3Fiso_floor_type%3Dhardwood; _ga_BPEVSBVR9J=GS1.2.1715176611.5.1.1715178696.0.0.0',
    'priority': 'u=0, i',
    'referer': 'https://melmart.com/products/?iso_floor_type=hardwood',
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

def get_urls(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    # print(response.status_code)
    soup = BeautifulSoup(response.content,'html.parser')
    data = []


    for link in soup.find_all(class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
        url = link.get('href')
        data.append(url)
    return data


def get_product_data(url):
 
    response = requests.get(url, cookies=cookies, headers=headers);
    # print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser");

    d={}
    title = soup.find('h2', class_='size-h2 color-primary product-brand').text.strip();
    # print(title)
    d['title'] = title

    brand = soup.find('h1', class_='product_title entry-title color-body weight-bold text-uppercase family-body').text.strip()
    d['brand'] =  brand

    sku = soup.find('span', class_='sku').text.strip()
    d['sku'] =  sku


    specs = {}

    specification = soup.find('table', class_='shop_attributes').find_all('tr')
        # print(specification)
    for item in specification:
            key = item.find('th', class_='product-attribute').text.strip()
            value = item.find('td').text.strip()
            specs.update({key:value})


    for i in  ['Bevel', 'Collection', 'Edge', 'Floor Type', 'Installation', 'Length', 'Plank Width', 'Radiant Heat', 'Thickness', 'Wear Layer', 'Packaging', 'Warranty', 'Underlayment']:
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
    d['Underlayment'] = specs['Underlayment']


    img = soup.select('.tpwpg-thumbnail img')
    # print(img)
    for i in img:
        alt = i['alt']
        src = i['src']
        d['image_name'] = alt
        d['images'] = src


        # Load_csv(d)
# ---------------------------------------------------------------

collections = {
     '0':'https://melmart.com/brands/savannah/',
     '1':'https://melmart.com/brands/savannah/page/2/'

   
}

for collection, url in collections.items():
  for u in get_urls(url):
    print(u)
    get_product_data(u)


