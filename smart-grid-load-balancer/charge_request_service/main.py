from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
LOAD_BALANCER_URL = "http://load_balancer:5002/dispatch"

@app.route('/charge', methods=['POST'])
def charge():
    ev_data = request.get_json()
    try:
        res = requests.post(LOAD_BALANCER_URL, json=ev_data)
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
