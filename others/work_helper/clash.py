# encode: utf-8
import base64
import json
import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

cache = dict()


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
    return proxies


def create_yaml(data):
    return dump(data, Dumper=Dumper, allow_unicode=True)


def read_yaml(stream):
    return load(stream, Loader=Loader)


def get_provider():
    return create_yaml(cache).encode()


def post_provider():
    cache.update(dict(proxies=process_sub()))
    return b"success"


get_handlers = dict(
    provider=get_provider,
)

post_handlers = dict(
    provider=post_provider,
)


class Param:

    def __init__(self, action: str = "provider", key: str = ""):
        self.action = action
        self.key = key

    def check(self) -> bool:
        return self.key == key


class ConfigHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        path = self.parse_path()
        if path.check():
            self._set_response()
            self.wfile.write(get_handlers[path.action]())
            logging.info("fetched {} items".format(len(cache.get('proxies'))))
            self.wfile.flush()
        else:
            self.send_response(401)

    def do_POST(self):
        path = self.parse_path()
        if path.check():
            self._set_response()
            self.wfile.write(post_handlers[path.action]())
            logging.info("update {} items".format(len(cache.get('proxies'))))
            self.wfile.flush()
        else:
            self.send_response(401)

    def parse_path(self):
        _path = self.path.strip()
        if _path.startswith("/"):
            _path = _path[1:]
        if _path.endswith("/"):
            _path = _path[:-1]
        data = _path.split("/", 2)
        return Param(*data)


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
    port = int(os.getenv("SERVER_PORT", "8080"))
    key = os.getenv("ACCESS_KEY", "iamfrommars")
    cache.update(dict(proxies=process_sub()))
    create_server()
