import json
import requests
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import os

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/api/v1/<payload>', methods=['GET', 'POST'])
def getPayload(payload):
    data = request.get_json(silent=True, force=True)
    print(type(payload))
    print(data)
    print(type(data))
    s = str(data).replace('\'','\\').replace('\"', '\\')
    if request.headers.get("Authorization") == "CachorroZika":

        engine = create_engine('postgresql://postgres:123456@serverioutility.hopto.org/teste')
        engine.execute(f"INSERT INTO cachorro (nome) VALUES ('{s}')")
        return jsonify({"payload": data})
    return "deu ruim"


# port = int(os.environ.get('PORT', 5050))
# app.run(host="0.0.0.0", port=port)

