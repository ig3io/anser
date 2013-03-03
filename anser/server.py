import socket


def tcp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def upd_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class Anser(object):
    def __init__(self, name, protocol='udp'):
        if protocol == 'tcp':
            return TCPServer(name)
        elif protocol == 'udp':
            return UDPServer(name)
        else:
            raise ValueError("{} protocol not supported".format(protocol))


def default_action(data, address):
    print "{} - {}".format(address, data)

class BaseServer(object):
    def __init__(self, name):
        self.name = name

    def run(self, ip, port, buffer_size, debug, action):
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.debug = debug
        if not action is None:
            self.action = default_action
        else:
            self.action = action


class UDPServer(BaseServer):
    def __init__(self, name):
        super(UDPServer, self).__init__()

    def run(self, ip='127.0.0.1', port=8080,
            buffer_size=1024, debug=False,
            action=None):
        super(UDPServer, self).run(ip, port, buffer_size,
                                   debug, action)
        self.socket = udp_socket()
        self.socket.bind((self.ip, self.port))
        self._listen()

    def _listen():
        if self.debug:
            print "UDP server listening at {}.{}".format(
                        self.socket_type.upper(),
                        self.ip,
                        self.port
                    )
        while True:
            data, addr = self.socket.recvfrom(self.buffer_size)
            self.action(data, addr)


class TCPServer(BaseServer):
    def __init__(self, anem):
        super(TCPServer, self).__init__()

    
    def run(self, ip='127.0.0.1', port=8080,
            buffer_size=1024, debug=False,
            action=None):
        super(TCPServer, self).run(ip, port, buffer_size,
                                   debug, action)
        self.socket = tcp_socket()
        self.socket.bind((self.ip, self.port))
        self._listen()

    def _listen():
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        while True:
            data = self.conn.recv(self.buffer_size)
            self.action(data, self.addr)
