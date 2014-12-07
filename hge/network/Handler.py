__author__ = 'Hossein Noroozpour'
import socketserver

from hge.core.Player import Player


class Handler(socketserver.BaseRequestHandler):
    users = dict()
    timeout = 3.0

    def handle(self):
        self.request.settimeout(self.timeout)
        player = Player(self.request)
        player.start()
        player.log()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), Handler)
    server.serve_forever()