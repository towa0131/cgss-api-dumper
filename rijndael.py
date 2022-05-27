from Crypto.Cipher import AES
from Crypto.Util import Padding

class Rijndael:
    @classmethod
    def encrypt_cbc(self, s, iv, key):
        aes = AES.new(key, AES.MODE_CBC, iv)
        return aes.encrypt(Padding.pad(s, 16))

    @classmethod
    def decrypt_cbc(self, s, iv, key):
        aes = AES.new(key, AES.MODE_CBC, iv)
        return Padding.unpad(aes.decrypt(s), 16)