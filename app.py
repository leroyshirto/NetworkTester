from flask import Flask, request, jsonify
import os
from datetime import datetime
import requests
app = Flask(__name__)

next_hop_url = os.environ.get('NEXT_HOP_URL', '')
max_depth = int(os.environ.get('MAX_DEPTH', 1))


@app.route("/ping")
def ping():
    next_hop_response = {}
    response = {
        'hostname': os.environ.get('HOSTNAME'),
        'remote_addr': request.remote_addr,
        'hop': next_hop_response
    }
    try:
        next_hop_response['request_start'] = datetime.utcnow()
        if next_hop_url:
            next_hop_response['last'] = False
            hop_resp = requests.get(url='%s/ping' % next_hop_url)
            next_hop_response['status_code'] = hop_resp.status_code

            if hop_resp.status_code is 200:
                next_hop_response['hop'] = hop_resp.json()
        else:
            next_hop_response['last'] = True
    except Exception as e:
        next_hop_response['error_message'] = str(e)
    finally:
        next_hop_response['request_end'] = datetime.utcnow()

    print(response)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
