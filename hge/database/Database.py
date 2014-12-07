__author__ = 'Hossein Noroozpour'
import pymysql


class Database():

    DATABASE_NAME = "hge"
    USERNAME = "root"
    PASSWORD = "mysqlproject"
    HOST = "localhost"
    SECURITY_TABLE = "hge_security"
    ID_FIELD = "id"
    SESSION_KEY_FIELD = "session_key"
    AES_KEY_FIELD = "aes_key"
    AES_IV_FIELD = "aes_iv"
    LAST_LOGIN_TIME_FIELD = "last_login_time"
    LOGIN_TRIES_FIELD = "login_tries"
    LAST_TRY_TIME_FIELD = "last_try_time"
    CREATE_TIME_FIELD = "create_time"
    LOGIN_STATE_FIELD = "login_state"

    def __init__(self):
        self.connection = pymysql.connect(
            host=self.HOST,
            user=self.USERNAME,
            passwd=self.PASSWORD,
            db=self.DATABASE_NAME)
        self.cursor = self.connection.cursor()
        print(self.cursor)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def fetch_row_with_id_query_creator(self, quests, table_name, row_id):
        return "SELECT {} FROM {} WHERE {} = {}".format(quests, table_name, self.ID_FIELD, row_id)

    def get_security_row(self, user_id):
        quests = "{}, {}, {}, {}, {}, {}, {}, {}".format(
            self.SESSION_KEY_FIELD,
            self.AES_KEY_FIELD,
            self.AES_IV_FIELD,
            self.LAST_LOGIN_TIME_FIELD,
            self.LOGIN_TRIES_FIELD,
            self.LAST_TRY_TIME_FIELD,
            self.CREATE_TIME_FIELD,
            self.LOGIN_STATE_FIELD
        )
        query = self.fetch_row_with_id_query_creator(quests, self.SECURITY_TABLE, user_id)
        self.cursor.execute(query)
        for row in self.cursor:
            result = dict()
            result[self.ID_FIELD] = user_id
            result[self.SESSION_KEY_FIELD] = row[0]
            result[self.AES_KEY_FIELD] = row[1]
            result[self.AES_IV_FIELD] = row[2]
            result[self.LAST_LOGIN_TIME_FIELD] = row[3]
            result[self.LOGIN_TRIES_FIELD] = row[4]
            result[self.LAST_TRY_TIME_FIELD] = row[5]
            result[self.CREATE_TIME_FIELD] = row[6]
            result[self.LOGIN_STATE_FIELD] = row[7]
            return result
        return None