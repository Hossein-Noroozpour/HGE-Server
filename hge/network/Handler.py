__author__ = 'Hossein Noroozpour'
import socketserver
import threading


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print("Server: ", data)
        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), Handler)
    server.serve_forever()