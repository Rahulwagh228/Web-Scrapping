
import requests
from lxml import html
import json

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
    return response.content

def extract_results(html_content,input_url):
    tree = html.fromstring(html_content)
    data = []
    json_data = tree.xpath('//script[@type="application/ld+json"]')[0]
    response_data = json.loads(json_data.text)
    name = response_data.get('name')
    url = response_data.get('url')
    brand = response_data.get('brand', {}).get('name')
    data_store = {
        'name':name,
        'brand':brand,
        'url':input_url
    }
    data.append(data_store)
    
    with open('wayfair.json','w') as file:
        json.dump(data,file,indent=4)



if __name__ == '__main__':
    input_url = input('Enter URL: ')
    data_url = extract_wayfair_data(input_url)
    html_content = extract_results(data_url, input_url)