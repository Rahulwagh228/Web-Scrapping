
import requests
from bs4 import BeautifulSoup
import json
import furl

def extract_wayfair_data(url):
    headers = {
    'authority': 'www.kohls.com',
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
    # cookies = {
    #     "ACCOUNT_CHOOSER":'AFx_qI5iSjsLJ2HWpx7o1riZryjSWk28Cijk8hCClwxH3rcJf1iWVItsnuFbCO6Kle8Dd8In0PsAHiV_h9KcS87P6MHL0fMfjYXjl90hoP6v-XvQ6WeBxiVA79kckk1OoPcu6AXh8uuChdJVPfDXx8ib_WQc8QOvwsIaZ7PoPOUjwEX4k0QJ0y-GyGSPhp0iNDHI1C-CSGDvHHHJtkbaCBq6ThoZtoFeA_3y4MW3qdtwOJlEMBbNgFSqU40xEDAz1v_fUW9qMozO1AK23ybYCtYx1bEaeXp3OI6lm6fS9ggJZke3Rg7OsVnxWaSkuQaxltfLivSUKltunkcomzecm7RwVgYWaw5XrqeLlgeXv2XVWxQvkjSI7nzBLXmbWgeUmLi0XRm-tYNznfbtKTmVzzjLXQpvtaqBaB-r4oRhSIDPP-gU5FNa2I4wr2L07o62XW_NA-xG_6HCRjABoM2X17zyGXtIHY38h-LB2mnCFKrEjt6LbX2VMLA',
    #     "APISID":'M_U2QCfTpQBp-L26/A-rJCftKmhXxhxh3Q',
    #     "LSID":"o.chat.google.com|o.chromewebstore.google.com|o.console.cloud.google.com|o.drive.fife.usercontent.google.com|o.drive.google.com|o.gds.google.com|o.groups.google.com|o.lens.google.com|o.mail.google.com|o.meet.google.com|o.myaccount.google.com|o.photos.fife.usercontent.google.com|o.photos.google.com|o.play.google.com|s.IN|s.blogger|s.youtube:g.a000igg_oK7S3jCF5p73mdcv2vRvNpQMraYBAjWvZ4CK2Xrbf0B0oaILoG8flSpCJRpbMpY-wgACgYKAbESAQASFQHGX2MilfTEOZXmBrdIf0t-jVjxjxoVAUF8yKoebr4oT9T8ruNV4dNwJVpI0076",
    #     "MUID":"16B8BEB82B0565D83D9AAAD92A9E64C8",
    #     "SAPISID":"DvgHl1gL2n7OdoL7/ANcibjRbn05d1N0_c",
    #     "SID":"g.a000igg_oEg3uiCHyu3Y2Sr3No7UdVw6AZEsfdPtbX7Nw2yw7YjPxEWnCXiqkJ9AH63P6JdBnAACgYKAQgSAQASFQHGX2MiXHDE0HKHxlLHY4Qn95HRRRoVAUF8yKqjjXsbj_R1DNs4uxSOTUWI0076",
    #     "SIDCC":"AKEyXzWm-0OigrmxB2Kq-bihh6ygqyWPtGxmvv-tl9Fp5yIGoCcCMw1bgN6ArE3PK4pPbJMy2l8",
    #     "SIDCC":"AKEyXzWa4RXz6mXuopk3VrAwr-UesIL-Og8b-52v0yFg91LEErBaLtVxvhUm7umwZM_qo1OInNQ",
    #     "__Host-1PLSID":"o.chat.google.com|o.chromewebstore.google.com|o.console.cloud.google.com|o.drive.fife.usercontent.google.com|o.drive.google.com|o.gds.google.com|o.groups.google.com|o.lens.google.com|o.mail.google.com|o.meet.google.com|o.myaccount.google.com|o.photos.fife.usercontent.google.com|o.photos.google.com|o.play.google.com|s.IN|s.blogger|s.youtube:g.a000igg_oK7S3jCF5p73mdcv2vRvNpQMraYBAjWvZ4CK2Xrbf0B0VUmBfcpD-uS7oIMbCvGzcwACgYKAWYSAQASFQHGX2MiU3RHgO3Wox-J6MthvIaCVhoVAUF8yKqSmOOKCm20y6Ml7Y1LGsV_0076",
    #     "__Host-GAPS":"1:W2CBiyL4suHbZ9tf1zN8Ao7cQ_Mqg8JmvHjfpdlFYiQysDX0YZLEo4RFgpXq2r7lD9d2n6pMqEw0BUjE51pzocxUUPYUpNhbqeZUxW5l_Y_0ZVDxhAzdFkiJ381P4EcJ4r-2gWz8apNhjw:urU22f9GtWgyi3Pk",
        
    # }
    cookies = {
        "_abck":"6F947539DF69DD15E8075C0B8610804C~-1~YAAQZvhWuFawQM6OAQAAf5OM3AuoLp3uU3HGvn6FQNQ1/WroWXMjyTY2dR9qglW4qlTnQfj/hZM31jtfNxITa7yA5ztuiSpTzjDJScQl3Vn/Ho6R5rkAFdxFAV2o3Q0Iin23utRcs8rprlPrYPoA2XfuQEwEAcq0Ywl+Z6ezbE/oF8yLYbTdEtYwNRf7OhK1DrCKPXQ3vl/aVYtbivbb7CsD/XCXxp5SGRO9gxide1yTeEjgK7K568H0aNiAf9TcYqdx+0z+ULVGSAg2FBohSTifFOQQi0qvfqmp0WfPyEy4bqwc1Ij8Zjjs2cwWrBmnotuCgYkgeFgJ/oPzIulQYnUu/Zxqun8E4bVertrPiNj8eMcJVeUoBrdk9ASfniacvmkvDgobYQc9pcQ17zo=~-1~-1~-1; Path=/; Domain=kohls.com; Secure; Expires=Mon, 14 Apr 2025 12:19:40 GMT",

        "ak_bmsc":"397D4D6ED2E5C82E9C73E5B6041136A7~000000000000000000000000000000~YAAQZvhWuFewQM6OAQAAf5OM3Bd4MhyZIaTcL7o865hmWVTxrpbE0GUCIW9SRCgzLlB+8WrETaSCeXY4p2j/sJI6nFI1S0FbrEnwHpRUwygdla017sU/Jv5obFNQrQceNl9n9AGKT4IiqB+NjHY8/u/clL7EFxRoPgOUXn2MvIqgNvUNr3AJ3nqC8IIAGTUdU/B2RZ8DjhMxbT5J5ZENDJyw7GOslX2uQebW08HMmBCrDa+Ng0Ck1zwZS3AuRUbEUQEjIpB3DLqae+U6tHKihoqnbS52jEdSaU0nI0SiNHsZKaH+pFuQ3ArmQ4bANZGiMaEp7V4wk51Nl1fSf4pLqFUgyxCRirFg4BNu/2gZd3Ag9UDlOmVrai+8; Path=/; Domain=kohls.com; Secure; Expires=Sun, 14 Apr 2024 14:19:38 GMT",

        "bm_sz":"14D14B8179F6CD8D627A61ADDC5A7D82~YAAQZvhWuFmwQM6OAQAAf5OM3BdrXioXuL4OhFgYum+EzbwiomgfpNVVjrSSJGeeTR22dAokII7XUxENDge65A0NqqWOxui3RLvN2t6Nh9trKcMBa0P9unyJ42iWNLRBzm/Q6eqIKRA5bf37V7ry8Q1q8G3c0LiuOnyGUoxDXaWps42nC+/wYi1jurtrMeQNDlo8+KfDonObihhl2GPUWbISEY0swlqYbwz8uaYOBf8S0W3lgz0mbJkZOXhlafymLxERbFwDuMCFstkmiYM956Wm2l3DLrytlQnNR17mgzO6lRjxoWsV+eSrtW1WKOd7X69np4aygKdjVfdrWInKgkLq6DoAPUA2Vd40MWRmkDejbo7JypuRnnp4~3618871~3618117; Path=/; Domain=kohls.com; Secure; Expires=Sun, 14 Apr 2024 16:19:38 GMT"
    }
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()
        # print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def extract_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())
    # read select json file 
    result = []
    with open('select_json.json','r') as file:
        json_data = json.load(file)
    for item in json_data:
        title = item.get('title', '')
        print(title)
        product_title = soup.find('h1', class_=title).text.strip()
        brand = item.get('brand', '')
        product_brand = soup.find('div', class_=brand).a.text.strip()
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
