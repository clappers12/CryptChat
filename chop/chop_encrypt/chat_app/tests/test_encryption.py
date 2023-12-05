# test_encryption.py
import unittest
from app.encryption.crypt_utils import CryptoUtils

class TestEncryption(unittest.TestCase):
    def test_rsa_encryption_decryption(self):
        # Test RSA encryption and decryption
        private_key, public_key = CryptoUtils.generate_rsa_keys()
        message = "Test Message"
        encrypted_message = CryptoUtils.encrypt_message(message, public_key)
        decrypted_message = CryptoUtils.decrypt_message(encrypted_message, private_key)
        self.assertEqual(message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
