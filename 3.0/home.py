

from bs4 import BeautifulSoup
import requests
import json
import re
import os
import pandas as pd

from urllib.parse import urljoin

myfile = "dixie-home-carpet.csv"
if os.path.isfile(myfile):
    os.remove(myfile)


def Load_Csv(d):
    df = pd.DataFrame(d, index=[2])
    if not os.path.isfile(myfile):
        df.to_csv(myfile, index=False)
    else:
        df.to_csv(myfile, mode='a', header=False, index=False)


def get_urls(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    select_element = soup.select_one('select.form-options')

    # Find all options within the select element
    options = select_element.find_all('option')

    # Extract and print the data-variant-id attributes
    get_data_urls = []
    # variant_ids = [option['data-variant-id'] for option in options]
    base_url_template = 'https://www.dixie-home.com/products/{product_name}?variant='
    for option in options:
        # Extract product name from the original URL
        product_name = url.split('/')[-1].split('#')[0]
        full_url = base_url_template.format(product_name=product_name) + str(option['data-variant-id'])
        get_data_urls.append(full_url)

    return get_data_urls


def extract_fabric_data(url,collection):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    d = {}

    d = {'Collection':collection}
    
    try:
        product_title = soup.find('h1',class_='product-title').text.strip()
        d['product_title'] = product_title
    except:
        d['product_title'] = ''

    try:
        sku = soup.find('div', class_='product-sku').find('span', {'data-product-sku': True}).text.strip()
        d['sku'] = sku
    except:
        d['sku'] = ''
    
    try:
        color_name = soup.find('span',class_='option-name').text.strip().replace('Color: ','')
        d['color'] = color_name
    except:
        d['color'] = ''

    try:
        product_description = soup.find(class_='product-description rte').text.strip()
        d['product_description'] = product_description
    except:
        d['product_description'] = ''
    specs = {}
    try:
        specifications = soup.find('ul',class_='product-features__list').find_all('li',class_='product-features__list-item')
        for item in specifications[1:]:
            title_element = item.find('span',class_='product-features__title')
            description_element = item.find('span',class_='product-features__description')
            if title_element and description_element:
                k = title_element.text.strip().replace(':', '')
                v = description_element.text.strip()
                specs.update({k: v})
    except:
        pass
        
    for i in ['Style', 'Color', 'Fiber Type', 'Construction Type', 'Carpet Width', 'Dye Method', 'Backing', 'Pattern Repeat', 'Stain and Soil Warranty', 'Texture Warranty', 'Abrasive Wear Warranty', 'Anti Static Warranty', 'Mftrng Defects Warranty', 'Country of Origin']:
        if i not in specs:
            specs[i] = ''
    d['Style'] = specs['Style']
    d['Color'] = specs['Color']
    d['Fiber Type'] = specs['Fiber Type']
    d['Construction Type'] = specs['Construction Type']
    d['Carpet Width'] = specs['Carpet Width']
    d['Dye Method'] = specs['Dye Method']
    d['Backing'] = specs['Backing']
    d['Pattern Repeat'] = specs['Pattern Repeat']
    d['Stain and Soil Warranty'] = specs['Stain and Soil Warranty']
    d['Texture Warranty'] = specs['Texture Warranty']
    d['Abrasive Wear Warranty'] = specs['Abrasive Wear Warranty']
    d['Anti Static Warranty'] = specs['Anti Static Warranty']
    d['Mftrng Defects Warranty'] = specs['Mftrng Defects Warranty']
    d['Country of Origin'] = specs['Country of Origin']



    #extract the warranty information
    warranty_information_sheets = soup.findAll('span', class_='product-features__title')
    for warranty_information_sheet in warranty_information_sheets:
        if 'Warranty Information:' in warranty_information_sheet.get_text():
            warranty_information_sheet_url = warranty_information_sheet.find_next('a')
            if warranty_information_sheet_url:
                warranty_info_url = warranty_information_sheet_url.get('href')
                d['Warranty Information'] = warranty_info_url
        else:
            d['Warranty Information'] = ''

    # Extract Product Specifications
    try:
        product_specification_sheets = soup.findAll('span', class_='product-features__title')
        for product_specification_sheet in product_specification_sheets:
            if 'Product Specifications Sheet:' in product_specification_sheet.get_text():
                product_specification_url = product_specification_sheet.find_next('a')
                if product_specification_url:
                    warranty_url = product_specification_url.get('href')
                    d['Product Specifications Sheet'] = warranty_url
            else:
                d['Product Specifications Sheet'] = ''
    except:
        d['Product Specifications Sheet'] = ''


    try:
        care_maintainance_sheets = soup.findAll('span', class_='product-features__title')
        for care_maintainance_sheet in care_maintainance_sheets:
            if 'Care, Maintenance & Warranty:' in care_maintainance_sheet.get_text():
                care_maintainance_sheet_url = care_maintainance_sheet.find_next('a')
                if care_maintainance_sheet_url:
                    cm_url = care_maintainance_sheet_url.get('href')
                    d['Care, Maintenance & Warranty'] = cm_url
            else:
                d['Care, Maintenance & Warranty'] = ''
    except:
        d['Care, Maintenance & Warranty'] = ''




    try:

        product_gallery = soup.find_all('img',class_='product-gallery--thumbnail')

        image_data = []
        url_pattern = 'https:'

        for img_tag in product_gallery:
            srcset_attribute = img_tag.get('srcset')
            
            if srcset_attribute:
                matches = re.findall(r'(\S+?) 4x', srcset_attribute)
                
                if matches:
                    image_src = url_pattern + matches[-1]  # Use the last match to get the highest resolution
                    image_data.append(image_src)
        try:
            color_images = image_data[0]
            d['color images'] = color_images
        except:
            d['color images'] = ''

        try:
            gallery_images = image_data[1:]

            # color_images = ''.join([color_img for color_img in color_images ])
            # print(color_images)
            gallery_images = ' | '.join([gallery_img for gallery_img in gallery_images ])
            
            
            d['gallery_images'] = gallery_images
        except:
            d['gallery_images'] = ''
    except:
        pass

    Load_Csv(d)




collections = {1: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-pyrenees#', 2: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-maroon-bells#', 3: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-bengal#', 4: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-natures-glen#', 5: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-shepherd#', 6: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-leigh-way#', 7: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-game-plan#', 8: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-chilton#', 9: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-teton#', 10: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-conqueror#', 11: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-big-idea#', 12: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-my-hero#', 13: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-smash-hit#', 14: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-finery#', 15: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-true-comfort#', 16: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-aspects#', 17: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-authentic#', 18: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-advocate#', 19: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-eminence#', 20: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-crossline#', 21: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-envy#', 22: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-amazing#', 23: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-modern-art#', 24: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-star-power#', 25: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-tactics#', 26: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-alluring#', 27: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-attributes#', 28: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-authentic-living#', 29: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-balance#', 30: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-big-dog#', 31: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-bombay#', 32: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-boston-common#', 33: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-brilliance#', 34: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-calm#', 35: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-calm-seas#', 36: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-cape-cod#', 37: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-capella#', 38: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-cassina#', 39: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-chromatic-touch#', 40: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-classic-demeanor#', 41: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-color-festival#', 42: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-colorworks#', 43: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-colter-bay#', 44: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-connection#', 45: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-contentment#', 46: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-cortana#', 47: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-costa#', 48: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-cozy#', 49: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-cypress#', 50: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-dawns-delight#', 51: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-delano#', 52: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-delight#', 53: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-dreamer#', 54: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-english-arbor#', 55: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-expressions#', 56: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-fantasia#', 57: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-fine-art#', 58: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-genteel#', 59: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-grand-isle#', 60: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-gusto#', 61: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-hearts-content#', 62: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-here-kitty#', 63: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-hideaway#', 64: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-innovations#', 65: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-inspiring#', 66: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-interlace#', 67: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-inviting#', 68: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-katies-comfort#', 69: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-labrador#', 70: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-larson#', 71: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-legit#', 72: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-magic-moment#', 73: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-marinette#', 74: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-millport#', 75: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-mindful#', 76: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-monteverde#', 77: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-morning-mist#', 78: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-my-style#', 79: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-mystique#', 80: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-natures-field#', 81: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-new-age#', 82: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-pop-art#', 83: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-prize-winner#', 84: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-rain-dance#', 85: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-rochelle#', 86: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-rock-creek#', 87: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-rockport#', 88: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-seagate#', 89: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-semitones#', 90: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-soft-silky#', 91: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-spectrum#', 92: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-spellbinding#', 93: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-spirit#', 94: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-spring-break#', 95: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-spring-fling#', 96: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-steadfast#', 97: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-sterling#', 98: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-suave#', 99: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-summer-breeze#', 100: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-summer-escape#', 101: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-suspicion#', 102: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-tabby#', 103: 'https://www.dixie-home.com/collections/carpet/products/dhfloors-in-taittinger#', 104: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-template#', 105: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-top-dog#', 106: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-top-notch#', 107: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-touch-of-velvet#', 108: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-traditions#', 109: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-treasured-moment#', 110: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-unique#', 111: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-vanburen#', 112: 'https://www.dixie-home.com/collections/carpet/products/dh-floors-in-victor#', 113: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-willow-lake#', 114: 'https://www.dixie-home.com/collections/carpet/products/dixie-home-in-yucatan#'}
for collection, url in collections.items():
  for u in get_urls(url):
    print(u)
    extract_fabric_data(u,collection)