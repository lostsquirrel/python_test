# coding=utf-8

import unittest

from kafka import TopicPartition, OffsetAndMetadata


class GeneralTest(unittest.TestCase):

    def test_topic_partition(self):
        for x in dir(TopicPartition('topic', 'partition')):
            print(x)


    def test_offset_and_metadata(self):
        for x in dir(OffsetAndMetadata(123, None)):
            print(x)
