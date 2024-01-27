from time import gmtime
from math import floor
from requests import get
import dateutil

import json


class Requester():
    def __init__(self, file, stop_point_id, line_id):
        self.file = file
        self.stop_point_id = stop_point_id
        self.line_id = line_id

    def request_next_passage(self):
        headers = {'apiKey' : 'tlsWi88p42EWWPuizf5epIlG20BVpwKl'}
        response = get(url=f"https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A{self.stop_point_id}%3A&LineRef=STIF%3ALine%3A%3A{self.line_id}%3A",
                       headers=headers)
        
        self._get_next_passage(response.json())
        
    def _get_next_passage(self, datas):
        with open(self.file, "r+") as file:
            data = json.load(file)
            data += datas
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        