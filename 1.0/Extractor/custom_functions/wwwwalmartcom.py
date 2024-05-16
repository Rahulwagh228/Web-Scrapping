
import requests
from lxml import html
import json

def extract_walmart_data(url):
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

    # cookies = {
    #     "set_cookie"s = "_pxhd=cIMwFOv877O9UQc78NLLc7Noa435X9fDqNMMWL6mpxJosDW27jYHrHRpQyceH/72D7Sx9PYE2otmUXg5pVNHmw==:gaOQ-b4/kAka1q8yqwWSeOwv058eXWEWSAytU2pn-nZsgU/rWauAGYEI2xVm//Qe0btm9AoU6jWX8IbnuogRTK/7SPbdsFRhahlIKkcln1c=;"
    # }
    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()
    return response.content

def extract_results(html_content, input_url):
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
        'url': input_url
    }
    data.append(data_store)
    
    with open('walmart.json','w') as file:
        json.dump(data,file,indent=4)



if __name__ == '__main__':
    input_url = input('Enter URL: ')
    data_url = extract_walmart_data(input_url)
    html_content = extract_results(data_url, input_url)