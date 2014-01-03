#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
try:
    import simplejson as json
except ImportError:
    import json
from anser import Client


def main():
    client = Client(address='127.0.0.1', port=8080, debug=True, default_category='default')
    client.send({
            "hello": "there"
        })


if __name__ == '__main__':
    main()
