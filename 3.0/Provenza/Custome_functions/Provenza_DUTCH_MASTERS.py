import requests


def extract_DUTCH_MASTERS():
    
    cookies = {
    '_fbp': 'fb.1.1715451064709.1590937354',
    '_iub_cs-56497403': '%7B%22timestamp%22%3A%222024-05-11T18%3A13%3A20.220Z%22%2C%22version%22%3A%221.60.1%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A56497403%2C%22cons%22%3A%7B%22rand%22%3A%2261f291%22%7D%7D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_fbp=fb.1.1715451064709.1590937354; _iub_cs-56497403=%7B%22timestamp%22%3A%222024-05-11T18%3A13%3A20.220Z%22%2C%22version%22%3A%221.60.1%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A56497403%2C%22cons%22%3A%7B%22rand%22%3A%2261f291%22%7D%7D',
        'origin': 'https://www.provenzafloors.com',
        'priority': 'u=1, i',
        'referer': 'https://www.provenzafloors.com/hardwood/detail?sku=PRO2803&color=Florence&collection=Volterra',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'attributeType': '',
        'attributeQuery': '',
        'tileType': 'Hardwood',
        'manufacturer': '',
        'collection': 'Volterra',
    }

    response = requests.post(
        'https://www.provenzafloors.com/api/ProductApi/getDetailInfoUsingCollection',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # print(data)

        list = []

        for  data in data:
            extracted_data_dict = {
                "color": data.get("color"),
                "collectionName": data.get("collectionName"),
                "imageUrl": data.get("imageUrl"),
                "brandName": data.get("brandName"),
                "description": data.get("description", {}).get("description"),
                "sku": data.get("tileDetail", {}).get("sku"),
                "species": data.get("tileDetail", {}).get("species"),
                "style": data.get("tileDetail", {}).get("style"),
                "grade": data.get("tileDetail", {}).get("grade"),
                "width": data.get("tileDetail", {}).get("width"),
                "length": data.get("tileDetail", {}).get("length"),
                "thickness": data.get("tileDetail", {}).get("thickness"),
                "finish": data.get("tileDetail", {}).get("finish"),
                "construction": data.get("tileDetail", {}).get("construction"),
                "installation": data.get("tileDetail", {}).get("installation"),
                "residentialWarranty": data.get("tileDetail", {}).get("residentialWarranty"),
                "coverage": data.get("tileDetail", {}).get("coverage")
            }
            list.append(extracted_data_dict)

    else:
        print("Failed to retrieve data from the API")
   
    print(list)
