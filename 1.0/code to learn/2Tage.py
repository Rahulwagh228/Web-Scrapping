import requests 
from bs4 import BeautifulSoup

# requests.get(url,)

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify())

# print(soup.title)
# print(soup.title.string)
# print(type(soup.findAll("div")))

for link in soup.find_all("a"):
    print(link.get("href"))