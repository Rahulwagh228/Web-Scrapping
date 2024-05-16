import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import unquote



myfile = 'regalhardwood.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)


cookies = {
    '_fbp': 'fb.1.1715451064709.1590937354',
    '_iub_cs-56497403': '%7B%22timestamp%22%3A%222024-05-11T18%3A13%3A20.220Z%22%2C%22version%22%3A%221.60.1%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A56497403%2C%22cons%22%3A%7B%22rand%22%3A%2261f291%22%7D%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_fbp=fb.1.1715451064709.1590937354; _iub_cs-56497403=%7B%22timestamp%22%3A%222024-05-11T18%3A13%3A20.220Z%22%2C%22version%22%3A%221.60.1%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A56497403%2C%22cons%22%3A%7B%22rand%22%3A%2261f291%22%7D%7D',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}


url = 'https://www.provenzafloors.com/hardwood/detail?sku=PRO047&color=Stonehenge&collection=Antico'
# url = 'https://www.provenzafloors.com/hardwood/detail?sku=PRO2318&color=Contour&collection=Affinity'

response = requests.get(url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

d = {}

# title = soup.find('div', class_='container clearfix').find_next('h1').text.strip()
# d['title'] = title
# print(title)

# Description with the naive approach
# href_value = soup.find('a', class_='social-icon si-borderless si-pinterest')['href']
# url_description_parts = href_value.split('description=', 1)
# desc = url_description_parts[1]
# d['description'] = desc

# color_raw = soup.find('title').text.strip()
# color = color.split(" ")[2] #This is a naive approach but for now it's working
# d['color'] = color

# Image = soup.find_all('li img')
# print(Image)


 
# API URL
# get navigation url
# https://www.provenzafloors.com/api/ProductApi/getTileNavigationData

# get the detailed 
# https://www.provenzafloors.com/api/ProductApi/getDetailInfoUsingCollection



   # for i in ['color', 'description', 'collectionName', 'imageUrl', 'brandName', 'sku', 'species', 'style', 'grade', 'width', 'length', 'thickness', 'finish', 'construction', 'installation', 'residentialWarranty', 'coverage']:
        #     if i not in extracted_data_dict:
        #         extracted_data_dict[i] = ' '
        # d['color'] = extracted_data_dict['color']
        # d['description'] = extracted_data_dict['description']
        # d['collectionName'] = extracted_data_dict['collectionName']
        # d['imageUrl'] = extracted_data_dict['imageUrl']
        # d['brandName'] = extracted_data_dict['brandName']
        # d['sku'] = extracted_data_dict['sku']
        # d['species'] = extracted_data_dict['species']
        # d['style'] = extracted_data_dict['style']
        # d['grade'] = extracted_data_dict['grade']
        # d['width'] = extracted_data_dict['width']
        # d['length'] = extracted_data_dict['length']
        # d['thickness'] = extracted_data_dict['thickness']
        # d['finish'] = extracted_data_dict['finish']
        # d['construction'] = extracted_data_dict['construction']
        # d['installation'] = extracted_data_dict['installation']
        # d['residentialWarranty'] = extracted_data_dict['residentialWarranty']
        # d['coverage'] = extracted_data_dict['coverage']