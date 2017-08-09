from flask import Flask, request, jsonify
import os
from datetime import datetime
import requests
import config

app = Flask(__name__)

current_depth = 1


@app.route("/ping")
def ping():
    global current_depth

    next_hop_response = {}
    response = {
        'hostname': os.environ.get('HOSTNAME'),
        'remote_addr': request.remote_addr,
        'hop': next_hop_response
    }
    try:
        next_hop_response['request_start'] = datetime.utcnow()
        if config.NEXT_HOP_URL and current_depth < config.MAX_DEPTH:
            next_hop_response['last'] = False
            hop_resp = requests.get(url='%s/ping' % config.NEXT_HOP_URL)
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
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
