# -*- coding: utf-8 -*-

import socket


def get_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)