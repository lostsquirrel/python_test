# coding=utf-8
import asyncio
import unittest

from asyncio_test import display_date


class SleepTests(unittest.TestCase):

    def test_run(self):
        asyncio.run(display_date())