
import requests
from bs4 import BeautifulSoup
import json
import furl
from urllib.parse import urlparse
from extractor_results.common_extract_result import extract_result

def extract_ulta_data(url):
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__ruid=b0734c1188be20136cd452a1cb47eab5; X_ULTA_VISITOR_ID=b0734c1188be20136cd452a1cb47eab5; X_ULTA_SITE=A; AKA_A2=A; ULTA_SITE=B; akaalb_alb_www_ulta=~op=WWW_ULTA_SITE_B:SiteB_Failover|~rv=37~m=SiteB_Failover:0|~os=6e40862a2abd586d46d773cd430ecffc~id=695527fe6d3ce1bf332937010f4ce9de; User-Agent=gomez; ULTASITE=en-us; ULTA_DSP_RT=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTYyMzgxOTQxODQsImlhdCI6MTcxMzY0NjE5NDE4NCwiYXVkIjoid3d3LnVsdGEuY29tIiwiaXNzIjoidWx0YS5jb20iLCJzdWIiOiJhZDM1ZmMwNC00YjY5LTRmOTItYjJlZS1jZTFkYTFkNGM3ZTUiLCJkZXZpY2VJZCI6ImVhOWYwOWMzLTg3NWYtNGZjMC1iZGQ3LTVlMjg1NjVjY2JmNCIsInNvZnRMb2dpblN0YXR1cyI6IkFub24ifQ.p-1acAXBsNdCfcg5EnuDLHVh9Y-1lV6kx5v-JUrWwPM; ULTA_DSP_AT=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM2NDcwOTU1OTUsImlhdCI6MTcxMzY0NjE5NTU5NSwiYXVkIjoid3d3LnVsdGEuY29tIiwiaXNzIjoidWx0YS5jb20iLCJzdWIiOiJhZDM1ZmMwNC00YjY5LTRmOTItYjJlZS1jZTFkYTFkNGM3ZTUiLCJkZXZpY2VJZCI6ImVhOWYwOWMzLTg3NWYtNGZjMC1iZGQ3LTVlMjg1NjVjY2JmNCIsImF1dGhTdGF0dXMiOiJBbm9uIiwic2Vzc2lvbklkIjoiN2E3MDNhZmYtZmM3Zi00N2U1LWE4YjgtMWZmNDhlNmYyMmYyIn0.EwNrJdiV3bBjRDEDewCF6u_r87MuaxaNzJq33Nzun6Y; utag_ck_gtid=undefined; powerreviews_reviews=charcoal detox mask : buttah skin; _gcl_au=1.1.1939536717.1713646197; _ga_LKM7RC8LP8=GS1.1.1713646197.1.0.1713646197.60.0.0; OptanonAlertBoxClosed=2024-04-20T20:49:57.310Z; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+21+2024+02%3A19%3A57+GMT%2B0530+(India+Standard+Time)&version=6.16.0&isIABGlobal=false&hosts=&consentId=5d7e86c5-becf-4629-b88f-9aff3e6754a8&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0001%3A1%2CC0007%3A1; s_fid=147CA24D9A6E85EF-230545CF5BF68867; __gads=ID=921894f21948a0ad:T=1713646197:RT=1713646197:S=ALNI_Ma5C0Ns1QTy0Q9RS-9-iZAK_utpzA; __gpi=UID=00000df45cd21923:T=1713646197:RT=1713646197:S=ALNI_MbpFoD8LYcgyvp2usqyUJSarZEjuA; __eoi=ID=0dc5aee6b55a67ea:T=1713646197:RT=1713646197:S=AA-AfjbGe6IFzeALWunO5r7rnufa; AMCVS_C218F16F55CC57607F000101%40AdobeOrg=1; gpv=buttah%20skin%3Acharcoal%20detox%20mask; _scid=fb08effc-e30a-49df-9f1f-ba862227e51c; _scid_r=fb08effc-e30a-49df-9f1f-ba862227e51c; _fbp=fb.1.1713646199122.61565183; _rdt_uuid=1713646200197.3e4bfe0c-aa10-43fa-b6ca-230b4e5edda9; _mibhv=anon-1713646200478-4599074335_8715; _caid=c19da021-b26b-427c-999e-1e7086f21578; _cavisit=18efd45f175|; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.ulta.com%252Fp%252Fcharcoal-detox-mask-pimprod2025809; ABTasty=uid=ys1y9pqc1pj6xgw8&fst=1713646203626&pst=-1&cst=1713646203626&ns=1&pvt=1&pvis=1&th=1099584.1363643.1.1.1.1.1713646204263.1713646204263.1.1_1111807.1378269.1.1.1.1.1713646204271.1713646204271.1.1; s_ecid=MCMID%7C81201192008955224172121151567582511715; s_cc=true; s_nr=1713646205183-New; AMCV_C218F16F55CC57607F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C19834%7CMCMID%7C81201192008955224172121151567582511715%7CMCAAMLH-1714250998%7C12%7CMCAAMB-1714250998%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1713653405s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; IR_gbd=ulta.com; IR_3037=1713646205636%7C123240%7C1713646205636%7C%7C; _derived_epik=dj0yJnU9eU9LWEVWQ2llQXBGTlVBb3FralhYYktucloxOTFhd0Ymbj1MNGpLa2hhRDg4UmNOUXdCOHAxQ1JnJm09ZiZ0PUFBQUFBR1lrS24wJnJtPWYmcnQ9QUFBQUFHWWtLbjAmc3A9NQ; _pin_unauth=dWlkPU0yWTFOR1JsWWpjdFl6bGtZaTAwTWprNExXRXlZMkV0TmpWbVlUTmlaakl6Wm1OaQ; distinct_id=f6e0a330-c530-5421-bb53-d86cca13a9a8; _ga=GA1.2.760908928.1713646197; _gid=GA1.2.1826583188.1713646207; __pdst=069d4eddbcc54dc8bb84c36731fd29f7; IR_PI=3356d40c-ff57-11ee-9d71-f79bba5ab296%7C1713646205636; _sctr=1%7C1713637800000; cto_bundle=gbRKa19kMk9wb1lNeld0c1JMcFR5RkhUSnJ2UzQwTFhNTm82OUQ4NUczZ0RrNEQzc1V4YzlwOVNocHVKS21TJTJGN3ZBVWlPWER2Y2JsUlB0N3RxUzZJWlUlMkJ5N0kzaFkxYVlGRlNjekFOMiUyQnNxJTJCYjlrVHJwJTJGckhUZjNhRUNEdU9nSmFyS2o2ZHBBVGZ1JTJGN09uV2ljS05YMlpIdHV1WSUyRkdrRkhwNjhibEpQSUNIR3A4cURrNXhyd0l5THZ2UDlzZTY0TWo1OSUyRlNodVRsR1olMkJCUWJSQlVzNHdNZm9BJTNEJTNE; mdLogger=false; kampyle_userid=fb1c-99d3-9375-bcbf-dde2-e27d-dd85-8d44; kampyleUserSession=1713646220469; kampyleUserSessionsCount=1; kampyleSessionPageCounter=1; RT="z=1&dm=ulta.com&si=0771c20a-06d3-4a55-869a-f07d19346ef0&ss=lv8koznm&sl=1&tt=q6z&bcn=%2F%2F684d0d48.akstat.io%2F&ld=qvl"; QuantumMetricSessionID=97e1bcecbe09bad5da6dde465a4f6638; QuantumMetricUserID=2ead099fa002144bfda20fb54bf2f626; utag_main=v_id:018efd45d21a0009cab2f0c8828c0506f003906700978$_sn:1$_se:9$_ss:0$_st:1713648096469$ses_id:1713646195228%3Bexp-session$_pn:1%3Bexp-session$vapi_domain:ulta.com; akavpau_vp-www-ulta-com=1713646606~id=b90c07fcd7408bf7fb103625f5cc5996; dtCookie=v_4_srv_26_sn_3EADD091789704FE4425B87410A0C833_perc_100000_ol_0_mul_1_app-3A6fe4664190660d01_0_app-3Aea7c4b59f27d43eb_0_rcs-3Acss_0',
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

def extract_ulta_results(html_content, input_url):
    return extract_result(html_content,input_url)
   