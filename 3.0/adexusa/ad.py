import requests
from bs4 import BeautifulSoup
cookies = {
    'PHPSESSID': 'n4u77q4l4925r95pa23809rgsg',
    '_gcl_au': '1.1.880731027.1715011326',
    '_ga': 'GA1.1.1888844669.1715011327',
    'woocommerce_recently_viewed': '104597',
    '_ga_Z7JK8J050P': 'GS1.1.1715011326.1.1.1715011357.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
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

response = requests.get('https://adexusa.com/product/field-tile-69/', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

tile_name = soup.find(class_='primary_font contenido__titulo sliderProducto').text.strip()
print(tile_name)
title = soup.find('div',class_='productSubtitle').text.strip()
specification = soup.find(class_='metas_icat').find_all('p')

specs = {}
href_values = [] 
for i in specification:
    span_tag = i.find_all('span')
    if len(span_tag) == 2:
        k = span_tag[0].text.strip().replace(':', '')
        href_values.append(k)
for i in ['Code', 'Collection', 'Color', 'Shape', 'Finish', 'Glaze', 'Edge']:
    if i not in specs:
        specs[i]
        # v = span_tag[1].text.strip()
        # specs.update({k:v})


href_values = [] 
for div_class in soup.find_all(class_='woocommerce-product-gallery__image'):
    a_tag = div_class.find('a')
    if a_tag and 'href' in a_tag.attrs:
        href_values.append(a_tag['href'])
img = ' | '.join(href_values)


