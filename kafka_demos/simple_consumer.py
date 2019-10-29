# coding=utf-8
import json
import multiprocessing
import threading
import time

from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata

from settings import topic, group_id, bootstrap_servers, kafka_message_encoding

# To consume latest messages and auto-commit offsets
kafka_topic_counter = 'jzwsd-dev-counter'
kafka_topic_camera_state = 'jzwsd-dev-camera-state'

kafka_group_id_counter = 'data-collector-counter'


class TestConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = multiprocessing.Event()
        self.setName('opc-resolver-counter-consumer')
        self.setDaemon(True)

    def run(self) -> None:
        consumer = KafkaConsumer(
            group_id=kafka_group_id_counter,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode(kafka_message_encoding)),
            enable_auto_commit=True)

        consumer.subscribe(topics=[kafka_topic_counter, kafka_topic_camera_state])
        while not self.stop_event.is_set():
            for message in consumer:
                # message value and key are raw bytes -- decode if necessary!
                # e.g., for unicode: `message.value.decode('utf-8')`
                print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                     message.offset, message.key,
                                                     message.value))
            # for x in dir(message):
            #     print(x)
            # consumer.commit({
            #     TopicPartition(topic, partition=message.partition): OffsetAndMetadata(message.offset + 1, None)
            # })


TestConsumer().start()
time.sleep(10)
