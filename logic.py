from time import gmtime
from math import floor
from requests import get
from dateutil.parser import isoparse

import dateutil
import time
import json

class Requester():
    def __init__(self, file: str):
        self.file = file

    def request_next_passage(self, stop_point_id: str, line_id: str):
        headers = {'apiKey': 'API-KEY'}
        response = get(url=f"https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A{stop_point_id}%3A&LineRef=STIF%3ALine%3A%3A{line_id}%3A",
                       headers=headers)
        
        self._get_next_passage(response.json())
        
    def _get_next_passage(self, datas):
        with open(self.file, "r+") as file:
            file.seek(0)
            json.dump(datas, file, indent=4)
            file.truncate()


class Timer():
    def __init__(self, file):
        self.file = file
        self.current_time = isoparse(self._convertISO(gmtime()))
        self.bus_time = ''
        self.delta = None
        self.difference = 0

    def _convertISO(self, t):
        return time.strftime("%Y-%m-%dT%H:%M:%S.000Z", t)
    
    def get_bus_time(self):
        with open(self.file, "r+") as file:
            data = json.load(file)
            bus_time = data["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][0]["MonitoredVehicleJourney"]["MonitoredCall"]["ExpectedArrivalTime"]
            self.bus_time = isoparse(bus_time)

            print(self.bus_time)

    def get_difference(self):
        self.delta = self.bus_time - self.current_time
        self.difference = floor(self.delta.seconds/60)
        return self.difference
