import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

myfile = 'regalhardwood.csv'
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_csv(d):
    df = pd.DataFrame(d,index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)




headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://regalhardwoods.com/floors',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



def get_urls(url):
    response = requests.get(url, headers=headers, verify=False)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    for links in soup.find_all('article', class_='brand-item'):
        urls = links.find('a')['href']
        data.append("https://regalhardwoods.com" + urls)
    print(data)
    return data

def extract_data(url):
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')




    d = {}

    # title
    title = soup.find('div', class_='text-holder').h1.text.strip()
    d['title'] = title

    desc = soup.find('div', class_='text').text.strip()
    d['description'] = desc

    specs = {}

    specification = soup.find(class_='info-list').find_all('li')

    for item in specification:
        name = item.find('span', class_='name').text.strip().replace(":", " ")
        value = item.find('span', class_='value').text.strip()
        specs[name.strip()] = value
        
    for i in ['Color Variation', 'Finish', 'Wear Layer', 'Width', 'Thickness', 'Length', 'Install Types', 'Warranty', 'Core', 'Color group']:
        if i not in specs:
            specs[i] = ' '
    d['Color Variation'] = specs['Color Variation']
    d['Finish'] = specs['Finish']
    d['Wear Layer'] = specs['Wear Layer']
    d['Width'] = specs['Width']
    d['Thickness'] = specs['Thickness']
    d['Length'] = specs['Length']
    d['Install Types'] = specs['Install Types']
    d['Warranty'] = specs['Warranty']
    d['Core'] = specs['Core']
    d['Color group'] = specs['Color group']


    # pdf link
    pdf_link = soup.find(class_='info-list').find_next('ul').find('a').get("href")
    d['pdf_link'] = pdf_link


    # Swatch image
    image = soup.find('div',class_='floor-visual box').find('div')

    if image:
        # Get the style attribute value
        style_value = image.get('style')
        
        if style_value:
            # Use regular expression to extract the URL
            match = re.search(r"url\(['\"]?([^'\")]+)['\"]?\)", style_value)
            
            if match:
                image_url = match.group(1)
            else:
                print("Background URL not found in style attribute")
        else:
            print("Style attribute not found in div tag")
    else:
        print("Div tag not found")

    d['swatch_img_url'] = image_url


    # floor Image
    try:
        floor_img = soup.find('div', class_='visual js-check-background')
        style_value1 = floor_img.get('style')
        match = re.search(r"url\(['\"]?([^'\")]+)['\"]?\)", style_value1)
        floor_img_url = match.group(1)
    except:
        floor_img_url = ''

    d['floor Image'] = floor_img_url

    Load_csv(d)



url = 'https://regalhardwoods.com/floors'

for u in get_urls(url):
    # print(u)
    extract_data(u)


