import requests
from time import sleep


result = None

while result != "ready":
    sleep(10)
    try:
        r = requests.get("http://localhost:8080/ors/v2/health")
        result = r.json()["status"]
    except:
        pass

print("Build Complete.")