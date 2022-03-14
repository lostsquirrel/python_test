# encoding: utf-8
# 测试使用base64
import base64

import unittest


class DemoTest(unittest.TestCase):

    def test_base(self):
        txt_file_name = "github_flow_bg.svg.txt"
        fl = open(txt_file_name)
        content = ""
        for x in fl:
            content += x

        xx = base64.b64decode(content)
        fx = open(txt_file_name[:-4], 'w')
        fx.write(xx)
        fl.close()
        fx.close()
        # print xx
        print('finished...........')

    def test_encode_file(self):
        filename = "/tmp/udp.conf"
        with open(filename, 'rb') as f:
            print(base64.b64encode(f.read()).decode())
