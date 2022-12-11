import json
from flask import Flask, jsonify, request

from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:29092"}

producer = Producer(conf)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({
        'message': 'hello world, from producers'
    })

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json(force=True)

    # producer.send('uber-rides', data)
    producer.produce('uber-rides', value=json.dumps(data).encode('utf-8'))
    
    return jsonify({
        "status": "success"
    })

app.run(host='0.0.0.0', port=8000)
print("Listening on port 8000 ...")