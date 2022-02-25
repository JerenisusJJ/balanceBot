import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://api.1cloud.ru/account"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer b6a4b41c89130dc52818512fc85ec9e0f41e6db12530e76541496e83e51c9da8"


resp = requests.get(url, headers=headers)
jsonData = json.loads(resp.text)

print(jsonData['Balance'])
