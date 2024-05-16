
import requests
from bs4 import BeautifulSoup
import json
import furl
from urllib.parse import urlparse
from extractor_results.common_extract_result import extract_result

def extract_nike_data(url):
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'anonymousId=A4F933B1223848DF2844E72D9B2BE134; AnalysisUserId=49.44.130.63.34459391709098825170; s_ecid=MCMID%7C69983483528392259547795287160413648881; _gcl_au=1.1.17840970.1709098836; bc_nike_india_triggermail=%7B%22distinct_id%22%3A%20%2218dee3aa25b2dd-05b7877a333d89-26001851-144000-18dee3aa25c67c%22%2C%22bc_persist_updated%22%3A%201709098836574%7D; _fbp=fb.1.1709098836880.1189570316; _pin_unauth=dWlkPU0yWTFOR1JsWWpjdFl6bGtZaTAwTWprNExXRXlZMkV0TmpWbVlUTmlaakl6Wm1OaQ; _ga_VZJN08LNK6=GS1.1.1709098836.1.1.1709099043.60.0.0; geoloc=cc=IN,rc=MH,tp=vhigh,tz=GMT+5.50,la=18.98,lo=72.83; audience_segmentation_performed=true; bm_mi=98301D5121800D3B209640B3DBB22082~YAAQB18sMUd5afeOAQAADH7U/BdOaHxW3+8+eamgZ0RWSF4IaUhLkRapvEIaRQFIULoN02zI4crJpz5mzTtBxdTlhHY5CfdoRXFY3VGBnWMlc8G+M++gMVHXOLtIrN2lm3+oxTIn2T+lYFFOIyjk7vLjubh2K6F6R1qXK3NDxhzqncP08jXv4HxMUFfU7toLGrjcX6gGGv54EwxZv5z5IZlBp3XJKYG0dPWwWO3Zvwetps29R4LRUkmVLcMQ7/Epzqu5aXXflfsTsiCrl5FCC9+88Q4ecVkcS+4F7UCqsY06Tq1mSaOaV3rimZyDlWYwvyEYOGWKFX9Nw0ed3rqL08oikWIqkwEyQ1ghc49gkr7mew==~1; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C69983483528392259547795287160413648881%7CMCAID%7CNONE%7CMCOPTOUT-1713645971s%7CNONE%7CvVersion%7C3.4.0%7CMCIDTS%7C19834%7CMCAAMLH-1714243571%7C12%7CMCAAMB-1714243571%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; ni_c=1PA=1|BEAD=1|PERF=1|PERS=1; sq=3; ppd=pdp|nikecom>pdp>nike%20court%20legacy%20next%20nature; cid=undefined%7Cundefined; _scid=da17a482-cc00-4de3-be09-36dce9b28640; _gid=GA1.2.2078544941.1713638776; nike_locale=us/en_us; CONSUMERCHOICE=us/en_us; CONSUMERCHOICE_SESSION=t; ak_bmsc=673BA44F24DBB0D7A8EFA21FE49B63AE~000000000000000000000000000000~YAAQxvhWuCURIOiOAQAAV7zU/BfszRsY1SuzzB/ZYPKB/mv1mIzVp8fWD2czLNKAXwXJvPp556GNUTHkmUOSuSu8D0kPBUQQ5AXwC2fMFlFbrFBzVszaN++lFhtPjMgvPpnTPupSiY6luFi8bHJs7ts6Z9WpDTZera50SqrwUtYxA78PNQ3drzp+TROcLLn+JGVFyh5+v/LmfiHBHoKa/SLuZm52aDE4vmosBnKkExtB8P3JrotBJXOJGl/kKes46vnWLXFOpwNLg8wnVLhiVmZHpsLcrGVKK4w9SY3/CG2BVFi3qbjjIQbV+eX8hCLNfQlpEkC8RsvyrzWp7rHmlfzTqDxpcF6eDVopvjf3dujETLNMz3yvOuPJA6TuAqsDWnHhs1cz72Ep2wVFeLb/SnfasrMW/BnDcrBbfQ+YLlCZqqjKfYFu44yrMDnBvKUu+no1R26BJIzPUr8U6lliG2AFYHnOM40ff6HWm8/gMn85byZRYwdgUvs09UIdCJgpWcP2bSeAj0nVpYn4T5Ms4ngxZZmxazVyHLZ1JA1Y7Cp7eE5J; AKA_A2=A; bm_sz=8E935804E309A33E7D7A637DE14CEE1F~YAAQLF8sMRIa3K+OAQAA+u4X/RcXx6qp7m2X6omUUged1cviUn5OThii+11SQWfxbmkr9dl9uN4XUpwS37Wl0Dgg8/x5Q6bl1FcLmeok95WS8+NRJJVIX1a8dTvojlrjZMEkifnGBZhUju6nUVIBthrDgBNMweQ3weSlv1JwyT7AmneSd7ZOKaT3VgDcCxOFGZvPWgVf0PzxfGdGSusSL8GJXyWsOLmVcT0zOpeNv9rfQej0ic4ziEacuco7Qowf7L6QKx+SeceYrj9DvCWZjyjpBMO5xs5hfVtIU65XpWK6M3/5cL3HUavL94AAjgRzQUl7k1UNSL5HVHYX1J4bwnZ5Tct8901C3QYMQWe+n63oghgVKdJx/mElEvIYs6mOy924473zYEKEXG6y3fhhvQdVhiu/WV5OJDFir9tjgVaS+nb1a0fUIg==~4343363~4539700; at_check=true; mbox=session#a80d10923c184228933913c4a33327ed#1713645055|PC#a80d10923c184228933913c4a33327ed.41_0#1776887995; bluecore_pdp_view=true; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%2218dee3aa25b2dd-05b7877a333d89-26001851-144000-18dee3aa25c67c%22%2C%22bc_persist_updated%22%3A%201713638776455%7D; bc_invalidateUrlCache_targeting=1713643195524; _scid_r=da17a482-cc00-4de3-be09-36dce9b28640; bluecoreNV=false; _derived_epik=dj0yJnU9WHBVRUlHWnQ2NnBzWUQyNE5Od0U5RVJPX3NLbEQyZ0Embj1tTzZHdlJOUHBadWtMRGUtZ25sYWVRJm09ZiZ0PUFBQUFBR1lrSHJ3JnJtPWYmcnQ9QUFBQUFHWWtIcncmc3A9NQ; RT="z=1&dm=www.nike.com&si=31488800-e79c-4eeb-9fb3-056f74687c31&ss=lv8iwozq&sl=1&tt=625&rl=1&bcn=%2F%2F684d0d46.akstat.io%2F"; _ga=GA1.2.65001176.1709098836; _abck=46F22A837C4655535E280D7B301EFC92~-1~YAAQLF8sMYsc3K+OAQAADkwe/QvMUd7JGeXbnQgkdM4oPkTKveBX+De21nh8pYk+nDEYNvATZesSNjMi3j0STJQLfTuoSPQ70B0rTGQpwOG0vsL2fQ/CfQgAHWaLy2Q5SUK4VqRHhUIOI2XzpUlB21S9bgnrZrWBWYq6ZJv2LQR8BwcbpxP0BxHzSzk2102hf3Ryy/3dHvognq7hNPwU4iNsk54vbiy6uIH25IP2AyDZD52kGr+rVD+135mrJi2XuiFrXo028SIg1is5nx5ekQ9sq79gpCQ9M55mdkHDyQPrrgqP7SaUdhXTgEOmDXD5e1PNapNE5WKPob29/zfbkScpAiGGWCl+Ne9zKEF8CQ9gcLQGaggZFA8kIwGPjXiJ+Ta6pFlFXm4EFn8RMhfOx46WP2WAf/SRcJclFrlYUH7gITDCzgZfg8hMYWhQGIHWkxyV4AxjKT8ARGpBq+RsM64ULve9mgy0xGLXd3A3WKYGcBVtYXhsjUTdQNQA7gmlrK1CuLut76X+e3LdnHUu9VtTQMom1g==~-1~-1~-1; _rdt_uuid=1713638776207.7d6432eb-aad7-4870-a025-5a23aa50041f; _ga_QTVTHYLBQS=GS1.1.1713643196.3.1.1713643606.52.0.0; _uetsid=450fd590ff4611ee88dfa133ada56e7f; _uetvid=e60c2260d5fb11eeaae3d9081137544b; bm_sv=A93B7ABD3DB45F7474F86B2666C0DE73~YAAQHvhWuBvXJd2OAQAA5VIe/Rd3ZE3e9JDwTtmyuBLkWlkoXkQWPjyeyxm26flaVKFGmbEGn+h9aayHMLNLOMz/GuNqnGlrpMfhdIqWdQxuXyirb5TGjj1n4G3szx8ygYcYs2Fxqnl+WW9bMeCnSjy2keef4Dqi1Lgx4m7RcBdOoayG3myoyW4vxmw8Znb1cKNDZI+5Aqp/rPjj3VtnKiRoWn1jWyQ3LQ3g3iZZA5DyOjXpoiuX5EnApgautCk=~1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.60", "Google Chrome";v="124.0.6367.60", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
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

def extract_nike_results(html_content, input_url):
    return extract_result(html_content,input_url)
   