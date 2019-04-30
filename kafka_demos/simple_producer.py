# coding=utf-8
import uuid
import random
import time
import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError

from settings import topic, group_id, bootstrap_servers

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
log = logging.getLogger(__name__)

n = 10

while n > 0:
    msg = uuid.uuid4().bytes
    # print(msg.hex())
    future = producer.send('my-topic', msg)
    delay = random.random()
    time.sleep(delay)
    # print(delay)
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    # Successful result returns assigned partition and offset
    print("%s:%d:%d: key=%s value=%s" % (record_metadata.topic, record_metadata.partition,
                                         record_metadata.offset, None,
                                         msg.hex()))

    n -= 1
producer.close()