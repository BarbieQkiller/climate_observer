import os
import time
import requests
import random

INFLUX_URL = os.getenv("INFLUX_URL")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
SENSOR_NAME = os.getenv("SENSOR_NAME")

while True:
    headers = {"Authorization": f"Token {INFLUX_TOKEN}"}
    data = f"weather,name={SENSOR_NAME} temp={random.randrange(10, 20)}"
    r = requests.post(INFLUX_URL, headers=headers, data=data)
    print(r.text)
    time.sleep(10)
