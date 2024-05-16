import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'neri_white.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)


cookies = {
    '_gcl_au': '1.1.1984890401.1715163425',
    '_ga': 'GA1.1.2122960987.1715163425',
    'PHPSESSID': 'fajcl615og94lja7a9sp6lqg9q',
    'woocommerce_recently_viewed': '104740%7C104597',
    '_ga_Z7JK8J050P': 'GS1.1.1715240391.7.1.1715240677.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.1984890401.1715163425; _ga=GA1.1.2122960987.1715163425; PHPSESSID=fajcl615og94lja7a9sp6lqg9q; woocommerce_recently_viewed=104740%7C104597; _ga_Z7JK8J050P=GS1.1.1715240391.7.1.1715240677.0.0.0',
    'priority': 'u=0, i',
    'referer': 'https://adexusa.com/familia/ceramic-tiles/page/3/?catalogo=general',
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

params = {
    'catalogo': 'general',
}



def get_urls(url):
    response = requests.get(url, cookies=cookies, headers=headers, params=params)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    data = []

    for link in soup.find_all(id='#index-140687 a.ajax_add_to_cart'):
        url = link.get('href')
        data.append(url)
    print(data)
    return data


def extract_data(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")

    d ={}

    try:
        title = soup.find('h1', class_='product_title entry-title').text.strip()
        # print(title)
        d['title'] = title
    except:
        tile_name = soup.find(class_='primary_font contenido__titulo sliderProducto').text.strip()
        # print(tile_name)
        d['tile_name'] = tile_name
        # print(url + "error in it..")


    # Extracting specifications
    specification = soup.find(class_='metas_icat').find_all('p')
    specs = {}
    for i in specification:
        span_tag = i.find_all('span')
        if len(span_tag) == 2:
            k = span_tag[0].text.strip().replace(':', '')
            v = span_tag[1].text.strip()
            specs[k] = v
    for i in ['Code', 'Collection', 'Color', 'Shape', 'Finish', 'Glaze', 'Edge']:
        if i not in specs:
            specs[i] = ' '
    d['Code'] = specs['Code']
    d['Collection'] = specs['Collection']
    d['Color'] = specs['Color']
    d['Shape'] = specs['Shape']
    d['Finish'] = specs['Finish']
    d['Glaze'] = specs['Glaze']
    d['Edge'] = specs['Edge']

    # Extracting image URLs
    href_values = [] 
    for div_class in soup.find_all(class_='woocommerce-product-gallery__image'):
        a_tag = div_class.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href_values.append(a_tag['href'])
    img = ' | '.join(href_values)

    d['image'] = img

    Load_csv(d)
  




collection = {
    '1':  'https://adexusa.com/series/neri/?subserie=White',
    # '2':  'https://adexusa.com/familia/ceramic-tiles/page/2/?catalogo=ge=general', 

    }


# print(collection)

for collection, url in collection.items():
  for u in get_urls(url):
    print(u)
    extract_data(u)


    # testing
# extract_data('https://adexusa.com/product/rail-molding-frame-corner-20/')


