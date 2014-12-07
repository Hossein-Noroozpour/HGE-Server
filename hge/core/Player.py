__author__ = 'Hossein Noroozpour'
from enum import IntEnum, unique
from hge.database.Database import Database
from hge.security.Connector import Connector


class Player():
    @unique
    class State(IntEnum):
        start = 0
        user_does_not_exist = 1
        unauthenticated = 2
        login_attacker = 3
        authenticated = 4
        in_play = 5

    def __init__(self, socket):
        self.state = self.State.start
        self.socket = socket
        self.database = Database()
        self.secure_connection = Connector(socket, self.database)

    def start(self):
        self.secure_connection.authenticate()

    def log(self):
        pass


if '__main__' == __name__:
    pass