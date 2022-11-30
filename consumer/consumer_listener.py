from kafka import KafkaConsumer
from utils import create_entry
from app import app

import json

consumer = KafkaConsumer('uber-rides', bootstrap_servers='localhost:9092')

with app.app_context():
    for msg in consumer:
        entry_data = json.loads(msg.value)
        create_entry(entry_data)
        print('added new entry', entry_data)