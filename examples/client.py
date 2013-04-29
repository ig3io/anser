import json
import socket


def main():
    udp_ip = '127.0.0.1'
    udp_port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = json.dumps({
        'body': 'Hello there!',
        'type': 'default'
        })
    sock.sendto(message, (udp_ip, udp_port))


if __name__ == '__main__':
    main()
