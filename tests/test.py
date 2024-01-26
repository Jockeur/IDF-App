import requests
import json


def jprint(content):
    text = json.dumps(content, sort_keys=True, indent=4)
    print(text)


headers = {'apiKey': 'API-KEY'}

response = requests.get(url="https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A419093%3A&LineRef=STIF%3ALine%3A%3AC00553%3A",
                        headers=headers)

jprint(response.json())