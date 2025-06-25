import requests
import random
import time

URL = "http://localhost:5000/charge"

for i in range(50):  # simulate 50 vehicles
    res = requests.post(URL, json={"ev_id": i})
    print(res.json())
    time.sleep(random.uniform(0.1, 0.5))  # simulate varied arrival
