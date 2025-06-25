from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define substations with their service ports
SUBSTATIONS = ['substation1:5001', 'substation2:5001']

def get_current_load(substation):
    metrics_port = "8000"
    host = substation.replace("5001", metrics_port)
    try:
        res = requests.get(f"http://{host}/metrics")
        for line in res.text.splitlines():
            if "substation_load" in line and not line.startswith("#"):
                return float(line.split()[-1])
    except Exception as e:
        print(f"Error contacting {host}: {e}")
        return float("inf")
    return 0.0

@app.route("/dispatch", methods=["POST"])
def dispatch():
    data = request.json
    loads = {s: get_current_load(s) for s in SUBSTATIONS}
    print("Current loads:", loads)

    target = min(loads, key=loads.get)
    try:
        response = requests.post(f"http://{target}/charge", json=data).json()
        return jsonify({"routed_to": target, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
