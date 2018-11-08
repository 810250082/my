# -*- coding: utf-8 -*-

from kafka import KafkaProducer
import json
import os
import time
from sys import argv

# KAFKA_CONSUMER = KafkaConsumer(bootstrap_servers=args.kafka_hosts, client_id='suibo-db', group_id=args.kafka_groupid,
#                                value_deserializer=lambda v: json.loads(v.decode('utf-8')), enable_auto_commit=True)

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])


def log(str):
    t = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
    print("[%s]%s" % (t, str))


def list_file(path):
    print('good')
    dir_list = os.listdir(path)
    for f in dir_list:
        producer.send('world', f)
        producer.flush()
        log('send: %s' % (f))


list_file(argv[1])
producer.close()
log('done')