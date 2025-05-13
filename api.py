import requests

url = "https://itsthisforthat.com/api.php?json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")