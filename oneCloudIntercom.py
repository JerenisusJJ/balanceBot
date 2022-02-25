import requests
import json
from requests.structures import CaseInsensitiveDict
from config import tokenInter

url = "https://api.1cloud.ru/account"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = tokenInter


resp = requests.get(url, headers=headers)
jsonData = json.loads(resp.text)

print(jsonData['Balance'])
