from base64 import b64decode, b64encode

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class AESCypher:
    def __init__(self, key_str):
        self.key = b64decode(key_str.encode("utf-8"))

    @staticmethod
    def pad_message(message):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message) + padder.finalize()
        return padded_data

    @staticmethod
    def unpad_message(padded_message):
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_data = unpadder.update(padded_message) + unpadder.finalize()
        return unpadded_data

    @staticmethod
    def generate_key():
        import os

        key = os.urandom(16)
        return b64encode(key).decode("utf-8")

    def encrypt(self, message):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        encryptor = cipher.encryptor()

        message_bytes = message.encode("utf-8")
        padded_message = self.pad_message(message_bytes)
        encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

        return b64encode(encrypted_message).decode("utf-8")

    def decrypt(self, encrypted_message_str):
        encrypted_message = b64decode(encrypted_message_str.encode("utf-8"))

        backend = default_backend()
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        decryptor = cipher.decryptor()

        decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
        unpadded_message = self.unpad_message(decrypted_message)

        return unpadded_message.decode("utf-8")
