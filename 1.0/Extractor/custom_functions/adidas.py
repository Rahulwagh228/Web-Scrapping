# # import requests
# # from bs4 import BeautifulSoup
# # import json

# # # Function to extract title and brand from HTML
# # def extract_title_and_brand(html_content):
# #     soup = BeautifulSoup(html_content, 'html.parser')
    
# #     # Extract title
# #     # title1 = soup.title.string.strip() if soup.title else None
    
# #     # Extract brand (assuming it's contained within a specific tag)
# #     # Replace 'span' with the appropriate tag containing the brand name
# #     # brand1 = soup.find('class_'=title).string.strip() if soup.find('span', class_='brand') else None

# #     title_selector = selectors.get('title')
# #     brand_selector = selectors.get('brand')

# #     title_element = soup.find(title_selector)
# #     brand_element = soup.find(brand_selector)
    
# #     title = title_element.string.strip() if title_element else None
# #     brand = brand_element.string.strip() if brand_element else None


# #     result = {
# #         'Title': title,
# #         'Brand': brand,
# #         # 'BrandClass': brand_class,
# #     }
    
# #     return result

# # # If you're fetching HTML content from a URL:
# # response = requests.get("https://www.adidas.com/us/handball-spezial-shoes/IG6194.html")
# # html_content = response.text

# # # For demonstration purposes, let's assume html_doc contains the HTML content
# # with open("sample.html", "r") as f:
# #     selectors = json.load()


# # # Extract title and brand from HTML
# # rerun= extract_title_and_brand(html_content)

# # # Print the results
# # # print("Title:", title)
# # # print("Brand:", brand)

# # print("Brand:", rerun)

# # -------------------------------------------------------------------------------------------------

# import requests
# from bs4 import BeautifulSoup
# import json

# # Function to extract title and brand from HTML
# def extract_title_and_brand(html_content, selectors):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     print(soup.prettify())

#     response_data = json.loads(selectors.text)

#     title = soup.find(class_=response_data.get('name')).text
#     brand = soup.find(class_ = response_data.get('brand')).text


    
#     # title_selector = selectors.get('title')
#     # brand_selector = selectors.get('brand')

#     # title_element = soup.find(title_selector)
#     # brand_element = soup.find(brand_selector)
    
#     # title = title_element.string.strip() if title_element else None
#     # brand = brand_element.string.strip() if brand_element else None

#     result1 = {
#         'Title': title,
#         'Brand': brand,
#     }
    
#     return result1

# # Load selectors from JSON file
# # with open("adidas.json", "r") as f:
# #     selectors = json.load(f)

# # If you're fetching HTML content from a URL:
# # response = requests.get("https://www.adidas.com/us/handball-spezial-shoes/IG6194.html")
# # html_content = response.text()
# # print(html_content)

# headers = {
# 'authority': 'www.walmart.com',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# 'accept-language': 'en-US,en;q=0.9',
# 'referer': 'https://www.walmart.com/blocked?url=L2lwL0NyaWN1dC1Kb3ktVWx0cmEtY29tcGFjdC1TbWFydC1DdXR0aW5nLU1hY2hpbmUvODM4MDUzNjM1&uuid=b7b268bb-f384-11ee-b9a6-74b3413fba59&vid=&g=b',
# 'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': '"Linux"',
# 'sec-fetch-dest': 'document',
# 'sec-fetch-mode': 'navigate',
# 'sec-fetch-site': 'same-origin',
# 'upgrade-insecure-requests': '1',
# 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#     }

# response = requests.get('https://www.adidas.com/us/handball-spezial-shoes/IG6194.html', headers=headers)
# # print(response)
# html_content = response.text
# # print(html_content)

# with open("adidas.json", "r") as f1:
#     # title = json.load(f1)
#     # brand = json.load(f1)
#     response_data = json.loads(f1.text)


# # Extract title and brand from HTML
# result = extract_title_and_brand(html_content, selectors=response_data)

# # # Print the results
# # print("Title:", result['Title'])
# # print("Brand:", result['Brand'])

# print(result)


# --------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import json

def extract_title_and_brand(html_content, response_data):
    soup = BeautifulSoup(html_content, 'html.parser')
    # response_data = json.loads(selectors.text)

    title = soup.find(class_=response_data.get('title')).text
    brand = soup.find(class_=response_data.get('brand')).text

    data = []

    result = {
        'Title': title,
        'Brand': brand,
         'url' : response_data.get('url').text()
    }
    
    data.append(result)

    with open('adidas.json','w') as file:
        json.dump(data,file,indent=4)

    return result


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


url = 'https://www.adidas.com/us/handball-spezial-shoes/IG6194.html'

response = requests.get(url, headers=headers)
html_content = response.text

# with open("adidas.json", "r") as f1:
#     response_data = json.loads(f1)

with open("adidas.json", "r") as f1:
    selectors_content = f1.read()

response_data = json.loads(selectors_content)

result = extract_title_and_brand(html_content, selectors=response_data)
print(result)
