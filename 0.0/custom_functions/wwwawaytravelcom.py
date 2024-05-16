
import requests
from bs4 import BeautifulSoup
import json
import furl
from urllib.parse import urlparse
from extractor_results.common_extract_result import extract_result

def extract_awaytravel_data(url):
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'COUNTRY=IN; COUNTRY_REGION=MH; LATITUDE=19.0748; LONGITUDE=72.8856; analytics_device_id=d61b1efb-0530-47c8-9f63-5d08eaa911d3; LOCATION=US_USD; ldUser=eyJraW5kIjoibXVsdGkiLCJkZXZpY2UiOnsia2V5IjoiZDYxYjFlZmItMDUzMC00N2M4LTlmNjMtNWQwOGVhYTkxMWQzIiwia2luZCI6ImRldmljZSIsInJlZ2lvbiI6Ik1IIiwic3RvcmVmcm9udCI6InVzIn19; initial_attribution_data={}; attribution_data={%22gclid%22:%22none%22%2C%22referrer%22:%22none%22%2C%22referring_domain%22:%22none%22%2C%22utm_campaign%22:%22none%22%2C%22utm_content%22:%22none%22%2C%22utm_medium%22:%22none%22%2C%22utm_source%22:%22none%22%2C%22utm_term%22:%22none%22}; _sp_ses.45ce=*; _ga=GA1.1.367353745.1713640378; FPID=FPID2.2.2qvE2VX0jPuT1vPe8CxiGybwp5CztjuzrxuUE8yrr90%3D.1713640378; FPLC=W5FzyAvki08JBSl%2FVnbIw12xr%2BKPkrIVD8ATBNBtT8Ja4pLHaGmY62ErQST2xW7H8PWHPIoHDMNTNlYnfwmbd6q6SbR67rWkjwvfO1xAmVdHhPBLrUWwY5v%2F1EwCKg%3D%3D; _ga_F6S0LVSC74=GS1.1.1713640378.1.1.1713640820.0.0.975444221; _sp_id.45ce=a88595d6396be0de.1713640377.1.1713640927.1713640377; muxData=mux_viewer_id=4d783476-7238-4082-9cca-e1941c0dd5e0&msn=0.3945820970104039&sid=d382d726-2d0c-4bd2-b995-08e82052ffde&sst=1713640741095&sex=1713642432795',
    'if-none-match': 'W/"3qkflpw72p7v9f"',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_awaytravel_results(html_content, input_url):
    return extract_result(html_content,input_url)
   