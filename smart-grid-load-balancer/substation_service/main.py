from flask import Flask, request, jsonify
from prometheus_client import Gauge, start_http_server
import time
import threading

app = Flask(__name__)
current_load = Gauge('substation_load', 'Current Load on Substation')
load_value = 0

@app.route('/charge', methods=['POST'])
def charge():
    global load_value
    load_value += 1
    current_load.set(load_value)
    time.sleep(2)  # Simulate charging delay
    load_value -= 1
    current_load.set(load_value)
    return jsonify({"status": "charged"}), 200

def expose_metrics():
    start_http_server(8000)

if __name__ == '__main__':
    threading.Thread(target=expose_metrics).start()
    app.run(host='0.0.0.0', port=5001)
