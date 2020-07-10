from kafka import KafkaConsumer
from pymongo import MongoClient
from json 

'''
The first argument is the topic, numtest in our case.
bootstrap_servers=[‘localhost:9092’]: same as our producer
auto_offset_reset=’earliest’: one of the most important arguments. It handles where the consumer restarts reading after breaking down or being turned off and can be set either to earliest or latest. When set to latest, the consumer starts reading at the end of the log. When set to earliest, the consumer starts reading at the latest committed offset. And that’s exactly what we want here.
enable_auto_commit=True: makes sure the consumer commits its read offset every interval.
auto_commit_interval_ms=1000ms: sets the interval between two commits. Since messages are coming in every five second, committing every second seems fair.
group_id=’counters’: this is the consumer group to which the consumer belongs. Remember from the introduction that a consumer needs to be part of a consumer group to make the auto commit work.
The value deserializer deserializes the data into a common json format, the inverse of what our value serializer was doing.
'''

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.numtest.numtest

for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))