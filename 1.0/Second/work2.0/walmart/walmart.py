
import requests
from bs4 import BeautifulSoup
import json
import furl

def extract_wayfair_data(url):
    headers = {
    'authority': 'www.wayfair.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
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

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    # print(response)
    return response.text

def extract_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # read select json file 
    print(soup.prettify())
    result = []
    with open('select_json.json','r') as file:
        json_data = json.load(file)
    for item in json_data:
        title = item.get('title', '')
        print(title)
        product_title = soup.find('h1', class_=title).text.strip()
        brand = item.get('brand', '')
        product_brand = soup.find('a', class_=brand).text.strip()
        url = item.get('url','')

        data_store = {
            'title':product_title,
            'brand':product_brand,
            'url':url
        }
        result.append(data_store)
    
    with open('result_output.json','w') as file:
        json.dump(result,file,indent=4,default=str)

if __name__ == '__main__':
    input_url = input('Enter URL: ')
    parsed_url = furl.furl(input_url)
    domain = parsed_url.host
    if domain in input_url:
        data_url = extract_wayfair_data(input_url)
        html_content = extract_results(data_url)
    #data_url = extract_wayfair_data('https://www.wayfair.com/furniture/pdp/gracie-oaks-photina-tv-stand-for-tvs-up-to-65-w004894664.html?piid=64124215')
    # html_content = extract_results(data_url)
