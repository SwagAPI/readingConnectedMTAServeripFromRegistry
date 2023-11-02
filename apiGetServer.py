import requests
import urllib.parse

import urllib.parse





def getServerData(ip, port):
    url = 'https://mtasa.com/api/'
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    try:
        for item in data:
            if item["ip"] == ip and int(port) == item["port"]:
                return item["ip"],item["port"],item["name"],item["players"],item["maxplayers"]
    except:
        print("[System] Failed to fetch server data.")

