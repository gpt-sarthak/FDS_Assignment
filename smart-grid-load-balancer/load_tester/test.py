### 4. load_tester/test.py

import requests
import threading

URL = 'http://localhost:4000/charge'

def send_request():
    try:
        requests.post(URL)
    except requests.exceptions.RequestException:
        pass

threads = []
for _ in range(100):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()