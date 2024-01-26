import time
from math import floor
import datetime as dt
from dateutil import parser

def convertISO(t):
    return time.strftime("%Y-%m-%dT%H:%M:%S.000Z", t)

bus_time_data = "2024-01-26T14:52:02.000Z"
bus_time = parser.isoparse(bus_time_data)

current_time = parser.isoparse(convertISO(time.gmtime()))

delta = bus_time - current_time

print(f'Le bus en direction de "Gare de Sucy-Boneuil" arrive à "Les bordes" dans : {floor(delta.seconds/60)} minutes')