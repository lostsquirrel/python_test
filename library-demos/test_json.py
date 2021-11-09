import json
import unittest


class TestJSON(unittest.TestCase):

    def test_dumps_loads(self):
        a = dict(abc=123)
        print(a)
        content = json.dumps(a)
        xx = json.loads(content)
        print(type(xx))