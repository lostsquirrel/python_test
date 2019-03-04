# -*- coding:utf-8 -*-
import random
import time
import SocketServer

mock_message = (
    ur'#1#K001|0X000020|停车事件|2013-01-01 01:01:01|1|192,213|\\192.168.1.2\haddate\20130101\td.ser;',
    u'#2#K001|2013-01-01 01:01:01|车道1=28#平均速度=78#密度=3&车道2=32#平均速度=57#密度=3;'
)
message_key_event = 0
message_key_counter = 1


def even_trigger():
    return random.randint(1, 100) < 5


class MockTcpServerHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        while True:
            msg = self.request.recv(1024)
            if len(msg) > 0:
                print(msg)
        #     if even_trigger():
        #         message_key = message_key_event
        #     else:
        #         message_key = message_key_counter
        #     self.request.sendall(mock_message[message_key].encode('utf-8'))
        #     time.sleep(1)


class MockTcpServer:

    def __init__(self, host, port):
        self.server = SocketServer.TCPServer((host, port), MockTcpServerHandler)

    def start(self):
        self.server.serve_forever()


if __name__ == '__main__':
    HOST, PORT = "192.168.5.252", 10000
    HOST, PORT = "127.0.0.1", 9999

    server = MockTcpServer(HOST, PORT)
    server.start()
