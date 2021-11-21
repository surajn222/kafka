# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
from datetime import datetime
# Define server with port
bootstrap_servers=['localhost:9092']

# Define topic name where the message will publish
topicName='topic_1'

# Initialize producer variable
producer=KafkaProducer(bootstrap_servers=bootstrap_servers)



# datetime object containing current date and time

# Publish text in defined topic
while True:
	now = datetime.now()
	producer.send(topicName, b'Hello from kafka at ' + str(now).encode() )
	print("Message sent =", str(now))
