import threading
import logging
import time
import json
from kafka import KafkaConsumer, KafkaProducer

# Create Class for Producer
# You can send and receive strings if you remove the value_serializer and value_deserializer from the code below.

class Producer(threading.Thread):
    daemon = True
    def run(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            producer.send('my-topic', {"dataObjectID": "test1"})
            producer.send('my-topic', {"dataObjectID": "test2"})
            time.sleep(1)

# Create Consumer Class
class Consumer(threading.Thread):
    daemon = True
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['my-topic'])
        for message in consumer:
            print (message)

def main():
    threads = [
        Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)
    
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()