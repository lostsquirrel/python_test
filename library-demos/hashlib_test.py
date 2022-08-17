
import hashlib
import unittest


class HashlibTest(unittest.TestCase):

    def test_sha256(self):

        m = hashlib.sha256()
        m.update(b"Nobody inspects")
        m.update(b" the spammish repetition")
        print(m.digest().hex())

    def test_sha256_new(self):
        h = hashlib.new('sha256')
        h.update(b"Nobody inspects the spammish repetition")
        print(h.hexdigest())

    def test_sha256_file(self):
        m = hashlib.sha256()
        with open("/tmp/date", 'rb') as f:
            m.update(f.read())
            print(m.hexdigest())
