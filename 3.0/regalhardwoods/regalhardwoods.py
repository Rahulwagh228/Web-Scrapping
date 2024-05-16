import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

myfile = 'melmart_hardwood_memoirs.csv'
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



url = 'https://regalhardwoods.com/elk-mountain/abrams'
response = requests.get(url, headers=headers, verify=False)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')




d = {}

title = soup.find('div', class_='text-holder').h1.text.strip()
# print(title)
# d['title'] = title


specs = {}

specification = soup.find(class_='info-list').find_all('li')
# print(specification)

for item in specification:
    name = item.find('span', class_='name').text.strip().replace(":", " ")
    value = item.find('span', class_='value').text.strip()
    specs[name.strip()] = value
    # d[name] = value
    
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


# print(d)



