# -*- coding:utf-8 -*-
import socket
import sys

HOST, PORT = "192.168.5.20", 61616
HOST, PORT = "192.168.5.252", 9999
HOST, PORT = "127.0.0.1", 9999
HOST, PORT = "192.168.5.20", 6666
# data = " ".join(sys.argv[1:])
msg_event = '1'
msg_counter = '2'


def parse_message(msg):
    msg = msg.replace(';', '')
    _msg = msg.strip().split("|")
    # print(_msg)
    _, msg_type, device = _msg[0].split("#")
    del _msg[0]
    if msg_type == msg_event:
        data = parse_event(_msg)
    else:
        data = parse_counter(_msg)

    data['device'] = device
    return data


def parse_event(event):
    event_type, event_type_name, event_time, event_zone, event_coordinate, video_path = event
    return dict(
        event_type=event_type,
        event_type_name=event_type_name,
        event_time=event_time,
        event_zone=event_zone,
        event_coordinate=event_coordinate,
        video_path=video_path
    )


def parse_counter(counter):
    counter_time, counter_detail = counter
    lanes = counter_detail.split("&")
    return dict(
        counter_time=counter_time,
        counter_lane=map(parse_lane, lanes)
    )


def parse_lane(lane):
    lane_name, avg_speed, density = lane.split("#")
    lane_data = dict(
        amount=lane_name,
        avg_speed=avg_speed,
        density=density
    )

    return {k: get_value(v) for k, v in lane_data.items()}


def get_value(item):
    return int(item.split("=")[1])


# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
sock.send('yhsd')
file = 'event.txt'
fh = open(file, 'a+')
while True:
    msg = sock.recv(1024 * 1024 * 5)
    if len(msg) > 0:
        content = msg.decode('gbk')
        print(content)
        fh.write(content.encode('utf-8') + '\n')
        fh.flush()
        # print(parse_message(msg))
