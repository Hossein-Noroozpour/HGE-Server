__author__ = 'Hossein Noroozpour'
import socketserver
import threading
from hge.network.Handler import Handler
import socket


class Server(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if '__main__' == __name__:
    HOST, PORT = "localhost", 0
    server = Server((HOST, PORT), Handler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    def client(server_ip, server_port, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))
        try:
            sock.sendall(bytes(message, "utf-8"))
            response = str(sock.recv(1024))
            print("Received: {}".format(response))
        finally:
            sock.close()

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
    server.shutdown()