import json
from flask import Flask, jsonify, request
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/', methods=['GET'])
def hello():
    return jsonify({
        'message': 'hello world, from producers'
    })

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json(force=True)

    producer.send('uber-rides', json.dumps(data).encode('utf-8'))

    return jsonify({
        "status": "success"
    })

app.run(host='0.0.0.0', port=8000)
print("Listening on port 8000 ...")