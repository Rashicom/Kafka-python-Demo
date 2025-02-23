import json
from kafka import KafkaProducer
import argparse

# fetch the topic from command line arguments
parser = argparse.ArgumentParser(description="Kafka Temperature Producer")
parser.add_argument("-t", "--topic", type=str, required=True, help="Topic to produce")
arg = parser.parse_args()

# define serializer
def serializer(message):
    return json.dumps(message).encode('utf-8')


# creating a kafka producer
"""
Proucer is publishing temperature realtime data to a temp-topic topic
temp-data topic can be consists multiple partitions
"""
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=serializer
    )

while True:
    # collect temperature location and value from the producer
    temp_location = input("Enter Location \n")
    temp_value = input("Enter Temperature \n")

    producer.send(arg.topic,{"loc":temp_location,"value":temp_value})
    producer.flush()

    print(f"Temperature data sent successfully to Kafka topic : {arg.topic}")
