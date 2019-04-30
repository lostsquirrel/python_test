# coding=utf-8
from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata

from settings import topic, group_id, bootstrap_servers



# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic,
                         group_id=group_id,
                         bootstrap_servers=bootstrap_servers,
                         enable_auto_commit=False)
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value.hex()))
    # for x in dir(message):
    #     print(x)
    consumer.commit({
        TopicPartition(topic, partition=message.partition): OffsetAndMetadata(message.offset + 1, None)
    })

