import requests
import json

# Define the URL and payload for the API request
url = 'https://www.provenzafloors.com/api/ProductApi/getTileNavigationData'
payload = {
    "attributeQuery": "",
    "attributeType": "",
    "collection": "Affinity",
    "manufacturer": "",
    "tileType": "Hardwood"
}

# Send the POST request to the API
response = requests.post(url, json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # List to store extracted information from each response object
    extracted_data_list = []
    
    # Loop through each response object
    for data in data:
        extracted_item = {
        "color": data.get("color"),
        "collectionName": data.get("collectionName"),
        "brandName": data.get("brandName"),
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

    
else:
    print("Failed to retrieve data from the API")
