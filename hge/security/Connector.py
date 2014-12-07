__author__ = 'Hossein Noroozpour'
from hge.core import Protocol


class Connector():
    def __init__(self, socket):
        self.socket = socket

    def fetch_id(self):
        user_id = Protocol.get_id(self.socket.recv(Protocol.id_size))
        return user_id

    def authenticate(self):
        user_id = self.fetch_id()
        print("user id is: ", user_id)

