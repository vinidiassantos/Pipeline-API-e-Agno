import requests

url = "https://api.nasa.gov/planetary/earth/imagery"

response = requests.get(url)

print(response.json())