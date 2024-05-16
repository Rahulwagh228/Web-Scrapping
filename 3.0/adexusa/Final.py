import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from furl import furl

myfile = 'melmart.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)

def outer_collection_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    outer_urls = []

    for links in soup.select('a.grid-subseries__link'):
        urls = links.get('href')
        outer_urls.append(urls)
    return outer_urls

def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    data = []
    data_links = soup.find_all('h5',class_='t-entry-title h5')
    for link in data_links:
        field_tile = link.a.text.strip()
        if field_tile == "Field Tile":
            url = link.a['href']
            data.append(url)
    return data

    # for link in soup.find_all(class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
    #     url = link.get('href')

def adexusa_product_data(url):
    cookies = {
        'PHPSESSID': 'n4u77q4l4925r95pa23809rgsg',
        '_gcl_au': '1.1.880731027.1715011326',
        '_ga': 'GA1.1.1888844669.1715011327',
        'woocommerce_recently_viewed': '104597',
        '_ga_Z7JK8J050P': 'GS1.1.1715011326.1.1.1715011357.0.0.0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'PHPSESSID=n4u77q4l4925r95pa23809rgsg; _gcl_au=1.1.880731027.1715011326; _ga=GA1.1.1888844669.1715011327; woocommerce_recently_viewed=104597; _ga_Z7JK8J050P=GS1.1.1715011326.1.1.1715011357.0.0.0',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://adexusa.com/series/neri/?subserie=White',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    d = {}
    tile_name = soup.find(class_='primary_font contenido__titulo sliderProducto').text.strip()
    d['Tile'] = tile_name
    title = soup.find('div',class_='productSubtitle').text.strip()
    d['Title'] = title
    specification = soup.find(class_='metas_icat').find_all('p')

    specs = {}
    for i in specification:
        span_tag = i.find_all('span')
        if len(span_tag) == 2:
            k = span_tag[0].text.strip().replace(':', '')
            v = span_tag[1].text.strip()
            specs.update({k:v})
   
    for i in ['Code', 'Collection', 'Color', 'Shape', 'Finish', 'Glaze', 'Edge']:
        if i not in specs:
            specs[i] = ''
    d['Code'] = specs['Code']
    d['Collection'] = specs['Collection']
    d['Color'] = specs['Color']
    d['Shape'] = specs['Shape']
    d['Finish'] = specs['Finish']
    d['Glaze'] = specs['Glaze']
    d['Edge'] = specs['Edge']
    
    href_values = [] 
    for div_class in soup.find_all(class_='woocommerce-product-gallery__image'):
        a_tag = div_class.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href_values.append(a_tag['href'])
    img = ' | '.join(href_values)
    d['images'] = img

    Load_csv(d)

d_urls = ['https://adexusa.com/series/neri/']
# 'https://adexusa.com/series/studio/',
# 'https://adexusa.com/series/riviera/',
# 'https://adexusa.com/series/habitat/',
# 'https://adexusa.com/series/levante/',
# 'https://adexusa.com/series/earth/',
# 'https://adexusa.com/series/ocean/',
# 'https://adexusa.com/series/hampton/',
# 'https://adexusa.com/series/mosaic/',
# 'https://adexusa.com/series/floor/']


for c,i in enumerate(d_urls):
    print(c,i)
    f = outer_collection_urls(i)
    for j, k in enumerate(f):
        print(j,k)
        s = get_urls(k)
        for x,z in enumerate(s):
            print(x,z)
            adexusa_product_data(z)

            
# get_urls('https://adexusa.com/series/neri/?subserie=White')