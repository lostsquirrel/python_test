# encode: utf-8
import base64
import json
import logging
import sys
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

keys = (
    ('remarks', 'name'),
    ('encryption', 'cipher'),
    ('',)
)


def process_sub():
    resp = requests.get(url)
    if resp.status_code == 200:
        content = resp.content.decode()[6:]
        if content is not None and len(content) > 2:

            decoded_content = base64.b64decode(content)
            data = json.loads(decoded_content.decode())
            proxies = []
            if 'servers' in data:
                servers = data.pop('servers')
                for server in servers:
                    proxy = dict(name=server["remarks"], cipher=server['encryption'], type="ss", udp=True,
                                 server=server["server"], password=server['password'], port=server['port'])
                    proxies.append(proxy)
                return proxies


def process_config(proxies):
    out = []
    for x in order:
        out.extend(filter(lambda p: p['name'].startswith(x), proxies))
    return proxies


def create_yaml(data):
    return dump(dict(proxies=data), Dumper=Dumper, allow_unicode=True)


def read_yaml(stream):
    return load(stream, Loader=Loader)


class ConfigHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        logging.info("fetched {} items".format(len(sub_source)))
        self.wfile.write(create_yaml(process_config(sub_source)).encode())
        self.wfile.flush()


def create_server():
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = HTTPServer(server_address, ConfigHandler)
    logging.info('Starting httpd on {}...\n'.format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    url = os.getenv("SUB_URL")
    order = os.getenv("ORDER").split(",")
    port = int(os.getenv("SERVER_PORT"))
    sub_source = process_sub()
    create_server()
