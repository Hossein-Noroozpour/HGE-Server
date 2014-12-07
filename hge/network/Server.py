__author__ = 'Hossein Noroozpour'
import socketserver
import socket

from hge.network.Handler import Handler


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    on_users = dict()


if '__main__' == __name__:
    test = 1
    if test == 0:
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
    elif test == 1:
        ip, port = "0.0.0.0", 8888
        server = Server((ip, port), Handler)
        ip, port = server.server_address
        server.serve_forever()
        server.shutdown()