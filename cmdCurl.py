import requests
import json
from requests.structures import CaseInsensitiveDict


def getBalance(urlReq, tokenReq, reqBool=0):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = tokenReq
    resp = requests.get(urlReq, headers=headers)
    if reqBool == 0:
        rawString = json.loads(resp.text)
        friedString = float(rawString['data']['real'])
        return friedString
    elif reqBool == 1:
        friedString = resp.text.replace(',', '.')
        #print()
        friedString = float(friedString)
        return friedString
