# import requests 

# def fetchdata (url, path):
#     r = requests.get(url)
#     with open (path, "w") as f:
#         f.write(r.text)


# url = "https://www.ajio.com/"

# fetchdata(url, "data/times.html")

# ---------------------------------------------------------------------------------------------------

import requests

def fetchdata(url, filename):
    response = requests.get(url)
    # response.raise_for_status()
    print(response)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)

url = "https://www.datacamp.com/tutorial/making-http-requests-in-python"
fetchdata(url, "data/times.html")


