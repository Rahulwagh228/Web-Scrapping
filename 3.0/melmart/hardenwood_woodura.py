import requests


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'melmart_hardwood.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)



def get_product_data(url):
    cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36',
    'ffvisitorids': '{"melmart":"4d652bf68c114b209333b19e79e05b46"}',
    'ffvendorids': '{"melmart":"bafa231287eb484dabfa8648c68d4692"}',
    '_ga': 'GA1.2.1471538261.1715146434',
    '_gid': 'GA1.2.11735546.1715146434',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fwoodura-xl-exclusive-walnut-nature-mel347033%2F',
    '_ga_BPEVSBVR9J': 'GS1.2.1715146435.1.1.1715146560.0.0.0',
    '__stripe_mid': 'dbf45703-7c27-4e74-bccc-c850781e7c987eee8f',
    '__stripe_sid': '2f9ae1d5-7e44-48ac-a8c7-03bc923f9eb129205b',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-08%2005%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2Fproducts%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36; ffvisitorids={"melmart":"4d652bf68c114b209333b19e79e05b46"}; ffvendorids={"melmart":"bafa231287eb484dabfa8648c68d4692"}; _ga=GA1.2.1471538261.1715146434; _gid=GA1.2.11735546.1715146434; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fwoodura-xl-exclusive-walnut-nature-mel347033%2F; _ga_BPEVSBVR9J=GS1.2.1715146435.1.1.1715146560.0.0.0; __stripe_mid=dbf45703-7c27-4e74-bccc-c850781e7c987eee8f; __stripe_sid=2f9ae1d5-7e44-48ac-a8c7-03bc923f9eb129205b',
        'priority': 'u=0, i',
        'referer': 'https://melmart.com/brands/woodura/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")


    d={}
    title = soup.find('h2', class_='size-h2 color-primary product-brand').text.strip()
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
     

    for i in ['Collection', 'Floor Type', 'Length', 'Plank Width', 'Radiant Heat', 'Thickness', 'Warranty', 'Packaging', 'Backing', 'Carb Phase 2 Compliant', 'Construction', 'Flammability', 'Formaldehyde Emission', 'Hardness', 'Impact Resistance', 'Profile', 'Slip Resistance (COF)', 'Sound resistance', 'Sustainability', 'Finish']:
        if i not in specs:
            specs[i] = ''

    d['Collection'] = specs['Collection']
    d['Floor Type'] = specs['Floor Type']
    d['Length'] = specs['Length']
    d['Plank Width'] = specs['Plank Width']
    d['Radiant Heat'] = specs['Radiant Heat']
    d['Thickness'] = specs['Thickness']
    d['Warranty'] = specs['Warranty']
    d['Packaging'] = specs['Packaging']
    d['Backing'] = specs['Backing']
    d['Carb Phase 2 Compliant'] = specs['Carb Phase 2 Compliant']
    d['Construction'] = specs['Construction']
    d['Flammability'] = specs['Flammability']
    d['Formaldehyde Emission'] = specs['Formaldehyde Emission']
    d['Hardness'] = specs['Hardness']
    d['Impact Resistance'] = specs['Impact Resistance']
    d['Profile'] = specs['Profile']
    d['Slip Resistance (COF)'] = specs['Slip Resistance (COF)']
    d['Sound resistance'] = specs['Sound resistance']
    d['Sustainability'] = specs['Sustainability']
    d['Finish'] = specs['Finish']

    # print(specs)
    img = soup.select('.tpwpg-thumbnail img')
    # print(img)
    for i in img:
        alt = i['alt']
        src = i['src']
        d['image_name'] = alt
        d['images'] = src

        Load_csv(d)

# url = "https://melmart.com/product/woodura-xl-exclusive-walnut-nature-mel347033/"

# get_product_data(url)


data_urls = [
    'https://melmart.com/product/woodura-xl-exclusive-walnut-nature-mel347033/',
    'https://melmart.com/product/woodura-xl-exclusive-walnut-terra-brown-mel347034/',
    'https://melmart.com/product/woodura-xl-nature-powder-white-mel347048/',
    'https://melmart.com/product/woodura-xl-oak-nature-earth-grey-mel0347025/',
    'https://melmart.com/product/woodura-xl-oak-nature-honey-mel347028/',
    'https://melmart.com/product/woodura-xl-oak-nature-mineral-grey-mel347026/',
    'https://melmart.com/product/woodura-xl-oak-nature-misty-white-mel347024/',
    'https://melmart.com/product/woodura-xl-oak-nature-natural-mel347027/'
]

for c, i in enumerate (data_urls):
    print(c, i)
    get_product_data(i)















# ---------------------------------------------------------------------------------------

# def get_urls(web_url):
#     response = requests.get(web_url)
#     print(response.status_code)
#     soup = BeautifulSoup(response.content,'html.parser')
#     data = []

#     for link in soup.find_all(class_='a.woocommerce-LoopProduct-link'):
#         url = link.get('href')
#         print(url)
#     #     url = link.get('href')
#     #     data.append(url)
#     # print(data)

# wurl = "https://melmart.com/brands/woodura/"
# get_urls(wurl)