# -*- encodeing: utf-8 -*-
'''
Created on 2015-03-19

@author: lisong
'''
import configparser
import unittest


class DemoTest(unittest.TestCase):

    def test_create(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'ServerAliveInterval': '45',
            'Compression': 'yes',
            'CompressionLevel': '9'
        }
        config['bitbucket.org'] = {}
        config['bitbucket.org']['User'] = 'hg'
        config['topsecret.server.com'] = {}
        topsecret = config['topsecret.server.com']
        topsecret['Port'] = '50022'     # mutates the parser
        topsecret['ForwardX11'] = 'no'  # same here
        config['DEFAULT']['ForwardX11'] = 'yes'
        with open('example.ini', 'w') as configfile:
            config.write(configfile)

    def test_read(self):
        config = configparser.ConfigParser()
        self.assertEqual(config.sections(), [])
        config.read('example.ini')
        self.assertEqual(len(config.sections()), 2)
        self.assertTrue('bitbucket.org' in config)
        self.assertEqual(config['bitbucket.org']['User'], 'hg')
        self.assertEqual(config['DEFAULT']['Compression'], 'yes')

        topsecret = config['topsecret.server.com']
        self.assertEqual(topsecret['ForwardX11'], 'no')


# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
# config.add_section('Section1')
# config.set('Section1', 'an_int', '15')
# config.set('Section1', 'a_bool', 'true')
# config.set('Section1', 'a_float', '3.1415')
# config.set('Section1', 'baz', 'fun')
# config.set('Section1', 'bar', 'Python')
# config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# # Writing our configuration file to 'example.cfg'
# with open('example.cfg', 'wb') as configfile:
#     config.write(configfile)
