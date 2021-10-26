import ipaddress
import unittest


class PathTests(unittest.TestCase):

    def testV4(self):
        ip = ipaddress.ip_address('192.168.0.1')
        print(ip)
        self.assertEqual(ip.version, 4)

    def testV6(self):
        ip: ipaddress.IPv6Address = ipaddress.ip_address('2001:db8::')
        print(type(ip))
        self.assertEqual(ip.version, 6)