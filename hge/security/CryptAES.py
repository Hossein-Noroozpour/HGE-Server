__author__ = 'Hossein Noroozpour'
import base64
from Crypto.Cipher import AES
from Crypto import Random


class CryptAES:
    BLOCK_SIZE = 16
    CHAR_CODING = "utf-8"

    def __init__(self, aes_key, aes_iv):
        self.key = aes_key
        self.iv = aes_iv
        self.pad = self.pkcs7_padding
        self.unpad = self.pkcs7_unpadding
        self.cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

    def zero_padding(self, d):
        return d + (self.BLOCK_SIZE - len(d) % self.BLOCK_SIZE) * chr(0)

    @staticmethod
    def zero_unpadding(d):
        for i in range(0, len(d)):
            if d[len(d) - (i + 1)] != 0:
                return d[:len(d) - i]

    def pkcs7_padding(self, d):
        return d + (self.BLOCK_SIZE - (len(d) % self.BLOCK_SIZE)) * chr(self.BLOCK_SIZE - (len(d) % self.BLOCK_SIZE))

    @staticmethod
    def pkcs7_unpadding(d):
        return d[:-ord(d[len(d) - 1:])]

    @staticmethod
    def bytes_to_string(d):
        s = ""
        for i in range(len(d)):
            s += chr(d[i])
        return s

    def encrypt(self, raw):
        if type(raw) != str:
            raise TypeError("Only string can be encrypted")
        d = self.pad(raw)
        return self.cipher.encrypt(d)

    def decrypt(self, enc):
        return self.unpad(self.cipher.decrypt(enc))

    def create_random_string(self, size: int) -> str:
        return base64.b64encode(Random.new().read(size))[:size].decode(self.CHAR_CODING)

if '__main__' == __name__:
    print(AES.key_size)
    print(AES.key_size)
    key = Random.new().read(CryptAES.BLOCK_SIZE)
    iv = Random.new().read(CryptAES.BLOCK_SIZE)
    c = CryptAES(key, iv)
    data = c.create_random_string(18)
    print(data)
    c = CryptAES(key, iv)
    data = c.encrypt(data)
    print(data, " ", len(data))
    data = c.decrypt(data)
    print(data)