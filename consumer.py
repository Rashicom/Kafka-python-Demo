import json
from kafka import KafkaConsumer
import argparse

parser = argparse.ArgumentParser("Temperature Consumer")
parser.add_argument("-t", "--topic", type=str, required=True, help="Topic to consume")
parser.add_argument("-u", "--usergroup", type=str, required=True, help="usergroup")
arg = parser.parse_args()


def process_message(message):
    pass

# kafka consumer
consumer = KafkaConsumer(
    arg.topic,
    group_id=arg.usergroup,
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"Start consuming on topic : {arg.topic}, usergroup : {arg.usergroup}")

try:
    for message in consumer:
        print(f"New Message : {message.value}")
except KeyboardInterrupt:
    print("Consumer Stopped")
finally:
    consumer.close()