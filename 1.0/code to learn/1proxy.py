import requests


http_proxy  = "http://35.185.196.38"
http_proxy2  = "http://103.131.232.9"

proxies = {
    "http": http_proxy,
    "http": http_proxy2
}

url = "https://www.ajio.com/men-sneakers/c/830207010"


r = requests.get(url, proxies=proxies)

print(r.json())