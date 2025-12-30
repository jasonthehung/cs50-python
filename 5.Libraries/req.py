import json

import requests

url = "https://itunes.apple.com/search?entity=song&limit=1&term=weezer"
response = requests.get(url)
print(json.dumps(response.json(), indent=2))
