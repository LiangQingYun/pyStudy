import requests

url = "http://example.com"
data = {"key1": "value1", "key2": "value2"}

with requests.post(url, data=data) as response:
    print(response.text)