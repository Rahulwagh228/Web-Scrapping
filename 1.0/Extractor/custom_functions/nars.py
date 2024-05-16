import requests
from bs4 import BeautifulSoup
import json

def extract_titlendBrand( html_content, response_data):
    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.find(class_= response_data.get('title')).text
    brand = soup.find(class_= response_data.get('brand')).text

    data = []

    result = {
        "title" : title,
        "brand" : brand,
        "url" : 'https://www.macys.com/shop/product/nars-afterglow-liquid-blush?ID=16164514&swatchColor=Orgasm'
    }

    data.append(result)

    with open ('outputnars.json', 'w') as file:
        json.dump(data, file)


headers = {
    'authority': 'www.walmart.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.walmart.com/blocked?url=L2lwL0NyaWN1dC1Kb3ktVWx0cmEtY29tcGFjdC1TbWFydC1DdXR0aW5nLU1hY2hpbmUvODM4MDUzNjM1&uuid=b7b268bb-f384-11ee-b9a6-74b3413fba59&vid=&g=b',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}


url = "https://www.macys.com/shop/product/nars-afterglow-liquid-blush?ID=16164514&swatchColor=Orgasm"

response = requests.get(url, headers=headers)
html_content = response.text


with open ("nars.json", "r") as f2:
    selectors_content = f2.read()

response_data = json.loads(selectors_content)

result = extract_titlendBrand(html_content, selectors_content)

