import requests
import json
BASE = "http://127.0.0.1:500/"



response = requests.get(BASE+"rawheel")
print(response.json())


