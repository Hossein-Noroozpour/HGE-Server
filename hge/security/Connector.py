__author__ = 'Hossein Noroozpour'
from hge.core import Protocol
from hge.database.Database import Database
from hge.security.CryptAES import CryptAES
import datetime
import enum
import socket as sock
from random import randrange


class Connector():
    @enum.unique
    class LoginState(enum.IntEnum):
        NOT_LOGGED_IN = 0
        ID_RECEIVED = 1

    class MaxLoginTryReached(Exception):
        def __init__(self, value=None):
            self.value = value

        def __str__(self):
            return self.value.__str__()

    MAX_LOGIN_TRY = 3
    SESSION_KEY_SIZE = 32

    def __init__(self, socket: sock.socket, database):
        self.state = self.LoginState.NOT_LOGGED_IN
        self.socket = socket
        self.database = database
        self.session_key = None
        self.cryptor = None

    def fetch_id(self):
        user_id = Protocol.get_id(self.socket.recv(Protocol.id_size))
        return user_id

    def authenticate(self):
        user_id = self.fetch_id()
        print("user id is: ", user_id)
        user_sec_row = self.database.get_security_row(user_id)
        print(user_sec_row)
        if user_sec_row[Database.LOGIN_TRIES_FIELD] > self.MAX_LOGIN_TRY and user_sec_row[
            Database.LAST_LOGIN_TIME_FIELD] < datetime.datetime.now() + datetime.timedelta(minutes=30):
            raise self.MaxLoginTryReached(user_sec_row)
        elif user_sec_row[Database.LOGIN_STATE_FIELD] == self.LoginState.NOT_LOGGED_IN:
            self.cryptor = CryptAES(user_sec_row[Database.AES_KEY_IV_FIELD][:CryptAES.BLOCK_SIZE],
                                    user_sec_row[Database.AES_KEY_IV_FIELD][CryptAES.BLOCK_SIZE:])
            self.session_key = self.cryptor.create_random_string(self.SESSION_KEY_SIZE +
                                                                 randrange(self.SESSION_KEY_SIZE))
            print(self.session_key)
            self.socket.sendall(self.cryptor.encrypt(self.session_key))
            self.session_key = self.session_key[:self.SESSION_KEY_SIZE]
            print(self.session_key)
            #wait for responce from client
            #decide
            #now update database
        elif user_sec_row[Database.LOGIN_STATE_FIELD] == self.LoginState.ID_RECEIVED:
            pass
