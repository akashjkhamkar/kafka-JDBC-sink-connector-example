import json
from flask import Flask, jsonify, request

from confluent_kafka import Producer

conf = {'bootstrap.servers': "broker:9092"}

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    print("Listening on port 8000 ...")