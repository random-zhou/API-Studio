
import requests
url = "https://oneapi.run.place/v1"
header = {
    'Authorization': 'Bearer sk-xxxxx',
    'Content-Type': 'application/json'
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "ÄãºÃ"}],
    "stream": False
}
resp = requests.post(url, headers=header, json=data, stream=True)
print(resp.json())