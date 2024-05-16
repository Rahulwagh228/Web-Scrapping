import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'adexusa.csv'
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
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    for link in soup.find_all('a', class_='grid-item__image-link'):
        url = link.get('href')
        data.append(url)
    # print(data)
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
    # print(d)
  




collection = {
    '1':  'https://adexusa.com/familia/ceramic-tiles/?catalogo=general',
    '2':  'https://adexusa.com/familia/ceramic-tiles/page/2/?catalogo=general',
    '3':  'https://adexusa.com/familia/ceramic-tiles/page/3/?catalogo=general', 
    '4':  'https://adexusa.com/familia/ceramic-tiles/page/4/?catalogo=general', 
    '5':  'https://adexusa.com/familia/ceramic-tiles/page/5/?catalogo=general', 
    '6':  'https://adexusa.com/familia/ceramic-tiles/page/6/?catalogo=general', 
    '7':  'https://adexusa.com/familia/ceramic-tiles/page/7/?catalogo=general', 
    '8':  'https://adexusa.com/familia/ceramic-tiles/page/8/?catalogo=general', 
    '9':  'https://adexusa.com/familia/ceramic-tiles/page/9/?catalogo=general',
    '10': 'https://adexusa.com/familia/ceramic-tiles/page/10/?catalogo=general', 
    '11': 'https://adexusa.com/familia/ceramic-tiles/page/11/?catalogo=general', 
    '12': 'https://adexusa.com/familia/ceramic-tiles/page/12/?catalogo=general', 
    '13': 'https://adexusa.com/familia/ceramic-tiles/page/13/?catalogo=general',
    '14': 'https://adexusa.com/familia/ceramic-tiles/page/14/?catalogo=general', 
    '15': 'https://adexusa.com/familia/ceramic-tiles/page/15/?catalogo=general', 
    '16': 'https://adexusa.com/familia/ceramic-tiles/page/16/?catalogo=general', 
    '17': 'https://adexusa.com/familia/ceramic-tiles/page/17/?catalogo=general', 
    '18': 'https://adexusa.com/familia/ceramic-tiles/page/18/?catalogo=general', 
    '19': 'https://adexusa.com/familia/ceramic-tiles/page/19/?catalogo=general', 
    '20': 'https://adexusa.com/familia/ceramic-tiles/page/20/?catalogo=general',
    '21': 'https://adexusa.com/familia/ceramic-tiles/page/21/?catalogo=general', 
    '22': 'https://adexusa.com/familia/ceramic-tiles/page/22/?catalogo=general',
    '23': 'https://adexusa.com/familia/ceramic-tiles/page/23/?catalogo=general', 
    '24': 'https://adexusa.com/familia/ceramic-tiles/page/24/?catalogo=general', 
    '25': 'https://adexusa.com/familia/ceramic-tiles/page/25/?catalogo=general', 
    '26': 'https://adexusa.com/familia/ceramic-tiles/page/26/?catalogo=general', 
    '27': 'https://adexusa.com/familia/ceramic-tiles/page/27/?catalogo=general', 
    '28': 'https://adexusa.com/familia/ceramic-tiles/page/28/?catalogo=general', 
    '29': 'https://adexusa.com/familia/ceramic-tiles/page/29/?catalogo=general', 
    '30': 'https://adexusa.com/familia/ceramic-tiles/page/30/?catalogo=general', 
    '31': 'https://adexusa.com/familia/ceramic-tiles/page/31/?catalogo=general', 
    '32': 'https://adexusa.com/familia/ceramic-tiles/page/32/?catalogo=general', 
    '33': 'https://adexusa.com/familia/ceramic-tiles/page/33/?catalogo=general', 
    '34': 'https://adexusa.com/familia/ceramic-tiles/page/34/?catalogo=general', 
    '35': 'https://adexusa.com/familia/ceramic-tiles/page/35/?catalogo=general',
    '36': 'https://adexusa.com/familia/ceramic-tiles/page/36/?catalogo=general',
    '37': 'https://adexusa.com/familia/ceramic-tiles/page/37/?catalogo=general', 
    '38': 'https://adexusa.com/familia/ceramic-tiles/page/38/?catalogo=general', 
    '39': 'https://adexusa.com/familia/ceramic-tiles/page/39/?catalogo=general', 
    '40': 'https://adexusa.com/familia/ceramic-tiles/page/40/?catalogo=general', 
    '41': 'https://adexusa.com/familia/ceramic-tiles/page/41/?catalogo=general', 
    '42': 'https://adexusa.com/familia/ceramic-tiles/page/42/?catalogo=general', 
    '43': 'https://adexusa.com/familia/ceramic-tiles/page/43/?catalogo=general', 
    '44': 'https://adexusa.com/familia/ceramic-tiles/page/44/?catalogo=general', 
    '45': 'https://adexusa.com/familia/ceramic-tiles/page/45/?catalogo=general', 
    '46': 'https://adexusa.com/familia/ceramic-tiles/page/46/?catalogo=general', 
    '47': 'https://adexusa.com/familia/ceramic-tiles/page/47/?catalogo=general', 
    '48': 'https://adexusa.com/familia/ceramic-tiles/page/48/?catalogo=general', 
    '49': 'https://adexusa.com/familia/ceramic-tiles/page/49/?catalogo=general', 
    '50': 'https://adexusa.com/familia/ceramic-tiles/page/50/?catalogo=general', 
    '51': 'https://adexusa.com/familia/ceramic-tiles/page/51/?catalogo=general', 
    '52': 'https://adexusa.com/familia/ceramic-tiles/page/52/?catalogo=general', 
    '53': 'https://adexusa.com/familia/ceramic-tiles/page/53/?catalogo=general', 
    '54': 'https://adexusa.com/familia/ceramic-tiles/page/54/?catalogo=general', 
    '55': 'https://adexusa.com/familia/ceramic-tiles/page/55/?catalogo=general', 

    }


# print(collection)

for collection, url in collection.items():
  for u in get_urls(url):
    print(u)
    extract_data(u)


    # testing
# extract_data('https://adexusa.com/product/rail-molding-frame-corner-20/')


