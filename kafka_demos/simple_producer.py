# coding=utf-8
import json
import uuid
import random
import time
import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError
from datetime import datetime
from settings import bootstrap_servers, JSONEncoder, kafka_message_encoding

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda m: json.dumps(m, cls=JSONEncoder).encode(
        kafka_message_encoding)
)
log = logging.getLogger(__name__)

n = 10
date_format = '%Y-%m-%d %H:%M:%S'
while n > 0:
    msg = dict(mgs=uuid.uuid4().bytes.hex(), xt=datetime.now().strftime(date_format))
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
                                         msg))

    n -= 1
producer.close()
