
import requests

url = "https://api.voxbone.com/v1/inventory/did"

headers = {
    "apikey": "Axxxx",
    "Accept": "application/json"
}

params = {
    "pageNumber": 0,
    "pageSize": 1,
    # optional filters - uncomment what you need
     "countryCodeA3": "GBR",
    # "serviceType": "VOXDID",  # or "VOX800" for toll-free
    # "e164Pattern": "%25123",  # numbers containing 123
    # "needAddressLink": False,
    # "smsOutbound": False,
    # "webRtcEnabled": False,
}

response = requests.get(url=url , params=params , headers=headers)

print(f"Status: {response.status_code}")


Data = response.json()
print(Data['dids'][0]['otherOptions'])