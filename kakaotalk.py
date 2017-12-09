#!/usr/bin/python3
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "text"
    }

    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"시작하기":
        dataSend = {
            "message": {
                "text": "아직 준비되지 않았습니다."
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "아직 준비되지 않았습니다."
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "아직 준비되지 않았습니다."
            }
        }

    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
