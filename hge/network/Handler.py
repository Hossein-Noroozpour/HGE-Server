__author__ = 'Hossein Noroozpour'
import socketserver
import threading


class Handler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        self.data = None

    def handle(self):
        self.data = self.request.recv(1024).strip()
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, self.data)
        print("Server: {} wrote.".format(self.client_address[0]))
        print("Server: response is {}.".format(response))
        print(self.data)
        self.request.sendall(self.data.upper() + bytes(response, "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), Handler)
    server.serve_forever()