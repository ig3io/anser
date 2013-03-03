import socket


class Anser(object):
    def __init__(self, name):
        self.name = name


    def run(self, ip='127.0.0.1', port='8053',
            buffer_size=1024, debug=False):
        self.ip = ip
        self.port = port
        self.debug = debug
        self.buffer_size = buffer_size
        self.socket = Anser._get_UDP_socket()
        self.socket.bind((self.ip, self.port))
        self._listen()
            

    def _listen(self):
        if self.debug:
            print "Listening at {}:{}".format(self.ip, self.port)
        while True:
            data, addr = self.socket.recvfrom(self.buffer_size)
            print "received data: {}".format(data)


    @staticmethod
    def _get_UDP_socket():
        return socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
                )

     
