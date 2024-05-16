import requests


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'melmart.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)


# def get_urls(web_url):
#     response = requests.get(web_url)
#     response.status_code
#     soup = BeautifulSoup(response.content,'html.parser')
#     data = []

#     for link in soup.find_all(class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
#         url = link.get('href')
#         print(url)
#     #     url = link.get('href')
#     #     data.append(url)
#     # print(data)



def get_product_data(url):

    cookies = {
        '_ga': 'GA1.2.883531671.1714537862',
        'ffvisitorids': '{"melmart":"fc624c71dc51460ab9b43085de5003fb"}',
        'ffvendorids': '{"melmart":"bafa231287eb484dabfa8648c68d4692"}',
        '_gid': 'GA1.2.950826261.1715101845',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-05-07%2016%3A40%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2024-05-07%2016%3A40%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36',
        '__stripe_mid': '4bac5fca-7572-4a5d-b083-166be2fe695a62724a',
        '__stripe_sid': '115d6c05-a83a-4a38-8bc6-b14ac3c8c67699effa',
        'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fevolution-bronze-oak-roxd4516ci%2F',
        '_ga_BPEVSBVR9J': 'GS1.2.1715101845.2.1.1715102056.0.0.0',
    }

    headers = {
        'authority': 'melmart.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '_ga=GA1.2.883531671.1714537862; ffvisitorids={"melmart":"fc624c71dc51460ab9b43085de5003fb"}; ffvendorids={"melmart":"bafa231287eb484dabfa8648c68d4692"}; _gid=GA1.2.950826261.1715101845; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-07%2016%3A40%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-07%2016%3A40%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmelmart.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36; __stripe_mid=4bac5fca-7572-4a5d-b083-166be2fe695a62724a; __stripe_sid=115d6c05-a83a-4a38-8bc6-b14ac3c8c67699effa; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmelmart.com%2Fproduct%2Fevolution-bronze-oak-roxd4516ci%2F; _ga_BPEVSBVR9J=GS1.2.1715101845.2.1.1715102056.0.0.0',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
  
    d = {}
    title = soup.find('h2',class_='size-h2 color-primary product-brand').text.strip()
    d['title'] = title

    brand = soup.find('h1', class_='product_title entry-title color-body weight-bold text-uppercase family-body').text.strip()
    d['brand'] =  brand

    # desc = soup.find('div', class_='description padding-top-reduced').find('p').text.strip()
    # d['description'] = desc

    sku = soup.find('span', class_='sku').text.strip()
    d['sku'] = sku
    
    specs = {}
 
    specification = soup.find('table', class_='shop_attributes').find_all('tr')
    for item in specification:
        key = item.find('th', class_='product-attribute').text.strip()
        value = item.find('td').text.strip()
        specs.update({key:value})

    for i in ['Collection', 'Thickness', 'Length', 'Bevel', 'Installation', 'Core', 'Packaging', 'Plank Width', 'Profile', 'Radiant Heat', 'Registered Emboss', 'Underlayment', 'Warranty', 'Finish', 'Impact Resistance', 'AC Rating']:
        if i not in specs:
            specs[i] = ''
    
    d['Collection'] = specs['Collection']
    d['Thickness'] = specs['Thickness']
    d['Length'] = specs['Length']
    d['Bevel'] = specs['Bevel']
    d['Installation'] = specs['Installation']
    d['Core'] = specs['Core']
    d['Packaging'] = specs['Packaging']
    d['Plank Width'] = specs['Plank Width']
    d['Profile'] = specs['Profile']
    d['Radiant Heat'] = specs['Radiant Heat']
    d['Registered Emboss'] = specs['Registered Emboss']
    d['Underlayment'] = specs['Underlayment']
    d['Warranty'] = specs['Warranty']
    d['Finish'] = specs['Finish']
    d['Impact Resistance'] = specs['Impact Resistance']
    d['AC Rating'] = specs['AC Rating']


    img = soup.select('.tpwpg-thumbnail img')
    for i in img:
        alt = i['alt']
        src = i['src']
        d['image_name'] = alt
        d['images'] = src



        Load_csv(d)




data_urls = ['https://melmart.com/product/cliffside-maple-mel01660/',
'https://melmart.com/product/coach-house-cherry-ch823/',
'https://melmart.com/product/ashtan-hickory-sh198/',
'https://melmart.com/product/lakeside-park-sail-rox85007-8/',
'https://melmart.com/product/lakeside-park-serene-rox3113-3/',
'https://melmart.com/product/lakeside-park-tranquil-rox3113-2/',
'https://melmart.com/product/new-york-oak-d8014nm/',
'https://melmart.com/product/lakeview-cottage-tan-roxhf057cb/',
'https://melmart.com/product/lakeview-light-house-roxhf059cb/',
'https://melmart.com/product/lakeview-muskoka-falls-roxd4193ck/',
'https://melmart.com/product/lakeview-pebble-beach-roxd2907cn/',
'https://melmart.com/product/lakeview-shoreline-roxhf055cb/',
'https://melmart.com/product/rio-oak-d4748nm/',
'https://melmart.com/product/coventry-87626/',
'https://melmart.com/product/sandstorm-89164-33/',
'https://melmart.com/product/hydroplank-river-bank-mel203-5/',
'https://melmart.com/product/hydroplank-sea-mel9621-1/',
'https://melmart.com/product/hydroplank-storm-mel203-2/',
'https://melmart.com/product/hydroplank-tide-mel9621-2/',
'https://melmart.com/product/lakeside-park-adirondack-rox3203/',
'https://melmart.com/product/lakeside-park-bayside-rox08032-1/',
'https://melmart.com/product/lakeside-park-boathouse-rox3201/',
'https://melmart.com/product/lakeside-park-canoe-rox81070-7/',
'https://melmart.com/product/lakeside-park-dockside-rox13148-3/',
'https://melmart.com/product/lakeside-park-oar-rox3011/',
'https://melmart.com/product/lakeside-park-oar-rox3011-2/',
'https://melmart.com/product/lakeside-park-paddle-rox85007-2/',
'https://melmart.com/product/colossus-espresso-rox109-9/',
'https://melmart.com/product/colossus-flint-rox5105/',
'https://melmart.com/product/colossus-latte-rox109-5/',
'https://melmart.com/product/colossus-natural-rox51502-2/',
'https://melmart.com/product/colossus-sand-rox51507-7/',
'https://melmart.com/product/colossus-steel-rox51502-6/',
'https://melmart.com/product/hydroplank-bay-mel203-4/',
'https://melmart.com/product/hydroplank-breakwater-mel1703-6/',
'https://melmart.com/product/hydroplank-cove-mel9621-16/',
'https://melmart.com/product/hydroplank-harbour-mel203-1/',
'https://melmart.com/product/hydroplank-ocean-mel203-3/',
'https://melmart.com/product/hydroplank-rapids-mel1703-1/',
'https://melmart.com/product/evolution-bronze-oak-roxd4516ci/',
'https://melmart.com/product/evolution-golden-oak-roxd4515ci/',
'https://melmart.com/product/evolution-pearl-oak-roxd4511ci/',
'https://melmart.com/product/evolution-prairie-oak-roxd6105cv/',
'https://melmart.com/product/evolution-sandstone-roxd4513ci/',
'https://melmart.com/product/evolution-snow-cap-roxd6101cv/',
'https://melmart.com/product/sound-chillout-oak-roxd3346-3d/',
'https://melmart.com/product/colossus-almond-rox51502-1/',
'https://melmart.com/product/colossus-bisque-rox51507-10/',
'https://melmart.com/product/colossus-blonde-rox51502-4/',
'https://melmart.com/product/colossus-chai-rox109-7/',
'https://melmart.com/product/colossus-coffee-rox51502-3/']
 
for c, i in enumerate(data_urls):
    print(c,i)
    get_product_data(i)

# collections = {

# '0':'https://melmart.com/brands/roxston/',
# '1':'https://melmart.com/brands/roxston/page/2/',
# '2':'https://melmart.com/brands/roxston/page/3/',
# '3':'https://melmart.com/brands/roxston/page/4/',
# '4':'https://melmart.com/brands/roxston/page/5/'

# }

# for collection, url in collections.items():
#   for u in get_urls(url):
#     print(u)
#     get_product_data(u,collection)