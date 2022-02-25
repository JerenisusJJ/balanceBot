import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://api.1cloud.ru/account"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer 9061c46bb811ac8c2345a545230944e7a1845666d0422d34f81e609e5b83d611"


resp = requests.get(url, headers=headers)
jsonData = json.loads(resp.text)

print(jsonData['Balance'])
