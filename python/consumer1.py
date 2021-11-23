# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import logging
logging.basicConfig(level=logging.INFO)
logging.info('The info message is displaying')

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name from where the message will recieve
topicName='topic_1'

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id='group1',bootstrap_servers=bootstrap_servers)

# Read and print message from consumer
for msg in consumer:
    logging.info("Topic Name=%s,Message=%s"%(msg.topic,msg.value))


