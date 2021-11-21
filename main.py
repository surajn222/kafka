cd /usr/local/kafka

List/Describe:
bin/kafka-topics.sh --list --zookeeper localhost:2181
bin/kafka-topics.sh --list --zookeeper localhost:2181 --exclude-internal
bin/kafka-topics.sh --zookeeper localhost:2181 --topic topic_1 --describe
bin/kafka-topics.sh --zookeeper localhost:2181 --describe --entity-type topics --entity-name my-first-topic
/bin/kafka-topics.sh --zookeeper localhost:2181 --describe --under-replicated-partitions

Create:
bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic topic_1 --partitions 3 --replication-factor 1
bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic topic_1 --partitions 3 --replication-factor 1 --if-not-exists


Configure/Alter topic:
bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic my-first-topic --partitions 5
#By default, a Kafka topic has a retention period of 7 days.
#This example shows the command to create a topic with a retention period of 10 seconds.
bin/kafka-topics --bootstrap-server localhost:9092 --create --topic my-topic-with-short-retention-period --partitions 3 --replication-factor 1 --config retention.ms=10000 --config segment.ms=10000
/bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-first-topic --add-config retention.ms=259200000
/bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-first-topic --add-config retention.ms=1000
/bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-first-topic --delete-config retention.ms
/bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-first-topic --add-config retention.ms=259200000
/bin/kafka-topics.sh --zookeeper localhost:2181 --describe --topics-with-overrides


Delete:
bin/kafka-topics.sh — zookeeper localhost:2181 --delete --topic topic_1

Producer:
usr/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic_1
/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-first-topic < topic-input.txt
/usr/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic_1 --property parse.key=true --property key.separator=:


Consumer:
/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic_1
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic some-topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-first-topic --from-beginning


Start Services:
bin/kafka-server-start.sh config/server.properties

Others:
/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic topic_1
/bin/kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic my-first-topic --time -2
/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic topic_1 --partitions partition-id, another-partition-id
