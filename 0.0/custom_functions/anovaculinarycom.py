
import requests
from bs4 import BeautifulSoup
import json
import furl
from urllib.parse import urlparse
from extractor_results.common_extract_result import extract_result

def extract_anovaculinary_data(url):
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'secure_customer_sig=; localization=US; cart_currency=USD; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _tracking_consent=%7B%22reg%22%3A%22%22%2C%22v%22%3A%222.1%22%2C%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%2C%22m%22%3A%22%22%7D%7D%2C%22region%22%3A%22INMH%22%7D; _shopify_y=81ab2e81-86fd-4a9b-8595-3aa440cfd8e7; _orig_referrer=; _landing_page=%2Fproducts%2Fanova-precision-cooker; receive-cookie-deprecation=1; _vwo_uuid_v2=DBE9069ABFC88FE3B1316EA1738255594|4f774d7dbdd6be763c6adf7c968a8755; _clck=e7an7p%7C2%7Cfl3%7C0%7C1571; cart=Z2NwLWFzaWEtc291dGhlYXN0MTowMUhWWUQ3MEFBVk43TTRES0U1RzRLRTFIUA; _pin_unauth=dWlkPU0yWTFOR1JsWWpjdFl6bGtZaTAwTWprNExXRXlZMkV0TmpWbVlUTmlaakl6Wm1OaQ; _fbp=fb.1.1713638705076.1193631521; _gid=GA1.2.686026565.1713638705; _pin_unauth=dWlkPU0yWTFOR1JsWWpjdFl6bGtZaTAwTWprNExXRXlZMkV0TmpWbVlUTmlaakl6Wm1OaQ; _gcl_au=1.1.644490713.1713638705; ajs_anonymous_id=8e648531-d0ba-4c9d-b430-f6c5a60519a6; locale_bar_accepted=1; intercom-id-p1hezn8i=be67cb6b-5570-4053-8808-5b7c27872a4a; intercom-session-p1hezn8i=; intercom-device-id-p1hezn8i=07b62b57-60c1-4d39-8c03-71045ee5c066; _shopify_sa_p=; _sp_ses.fe32=*; shopify_pay_redirect=pending; cart_sig=3d60e34512c8e24751ccd4a1f25b6a77; keep_alive=4db6d93a-9ccc-4e43-ad21-85f9ee2128f4; _rdt_uuid=1713638703667.aa8fdcd7-b494-4b2a-89c1-d410dba5dc5a; _shopify_s=35b8a908-7a4b-44a7-95c9-89f6f1ec29a1; _shopify_sa_t=2024-04-20T21%3A02%3A20.655Z; _derived_epik=dj0yJnU9ZEh6aEFldTVRTW1uOWk2VENtbWJVLXhJdzhZNG5lM3kmbj04ZHBiUTdQbDRsUVRiMnlLRnJ4U1l3Jm09ZiZ0PUFBQUFBR1lrTFYwJnJtPWYmcnQ9QUFBQUFHWWtMVjA; _ga_P30JN1M27B=GS1.1.1713646911.2.1.1713646943.28.0.0; __kla_id=eyJjaWQiOiJPV0psWVdZek9USXROemt5TVMwME1HSXdMV0kxT1dVdFpEQXhaalUxWm1ZNVpUUXciLCIkcmVmZXJyZXIiOnsidHMiOjE3MTM2Mzg3MDQsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYW5vdmFjdWxpbmFyeS5jb20vcHJvZHVjdHMvYW5vdmEtcHJlY2lzaW9uLWNvb2tlciJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxMzY0Njk0NCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9hbm92YWN1bGluYXJ5LmNvbS9wcm9kdWN0cy9hbm92YS1wcmVjaXNpb24tY29va2VyIn19; _ga=GA1.2.1522425008.1713638705; _derived_epik=dj0yJnU9SjhQUHBYaXhiQzBLa2lNTnloZ2FLRUJGZWNPQlFxVXImbj1yOWZhd0ZvVEJlUFZIOHhUZTRPd0tnJm09ZiZ0PUFBQUFBR1lrTFdRJnJtPWYmcnQ9QUFBQUFHWWtMV1Emc3A9Mg; _clsk=phxu5f%7C1713646949109%7C2%7C1%7Cl.clarity.ms%2Fcollect; _uetsid=1b44b430ff4611ee97fe91b1d96611c7; _uetvid=1b451e20ff4611ee979a5919d3f8ac4a; AMP_4ea5fb67e1=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1ZjVlNTAzMC05OGMyLTQ1MjYtYWU1OC05YjM2OWVlZmVjYzAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJ3MHFiM2Z5b3RrdGxicWwlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzEzNjQ2OTI4MTk4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxMzY0Njk2NzkxNCUyQyUyMmxhc3RFdmVudElkJTIyJTNBNCU3RA==; cart_ts=1713646970; tracker_device=acaa5f9c-c230-4561-96a9-35fc38fefd75; _sp_id.fe32=4d18fc29ca5ba9d6.1713638706.2.1713647208.1713638722',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_anovaculinary_result(html_content,input_url):
    return extract_result(html_content,input_url)



