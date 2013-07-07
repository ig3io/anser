# -*- coding: utf-8 -*-

import socket
try:
    import simplejson as json
except ImportError:
    import json
from . import utils


class Client(object):
    def __init__(self, address, port, default_category=None, debug=False):
        self.address = address
        self.port = port
        self.socket = utils.get_udp_socket()
        self.default_category = default_category
        self.debug = debug

    def send(self, message, category=None):
        if category is None:
            category = self.default_category
        message = json.dumps({
                "category": category,
                "message": message
                });
        self.socket.sendto(message.encode(), (self.address, self.port))