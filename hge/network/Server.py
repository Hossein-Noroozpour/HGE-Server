__author__ = 'Hossein Noroozpour'
import socketserver
from hge.network.Handler import Handler
import socket


class Server(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if '__main__' == __name__:
    import os
    ip, port = "localhost", 8888
    pid = os.fork()
    if 0 != pid:
        server = Server((ip, port), Handler)
        ip, port = server.server_address
        server.serve_forever()
    else:
        def client(server_ip, server_port, message):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((server_ip, server_port))
            try:
                sock.sendall(bytes(message, "utf-8"))
                response = str(sock.recv(1024))
                print("Client: {}".format(response))
            finally:
                sock.close()
        client(ip, port, "Hello World 1")
        client(ip, port, "Hello World 2")
        client(ip, port, "Hello World 3")