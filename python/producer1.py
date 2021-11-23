# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
from datetime import datetime
import time
import logging
logging.basicConfig(level=logging.INFO)
logging.info('The info message is displaying')

# Define server with port
bootstrap_servers=['localhost:9092']

# Define topic name where the message will publish
topicName='topic_1'

# Initialize producer variable
producer=KafkaProducer(bootstrap_servers=bootstrap_servers)

# Publish text in defined topic
while True:
	now = datetime.now()
	time.sleep(1)
	producer.send(topicName, b'Hello from kafka at ' + str(now).encode() )
	logging.info("Message sent = %s", str(now))
