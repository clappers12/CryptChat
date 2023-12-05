from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

class CryptoUtils:
    @staticmethod
    def generate_rsa_keys(key_size=2048):
        """
        Generates a new RSA private and public key pair.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_key(key, is_private=False, password=None):
        """
        Serializes a key to PEM format.
        """
        if is_private:
            if password:
                encryption = serialization.BestAvailableEncryption(password.encode())
            else:
                encryption = serialization.NoEncryption()
            return key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=encryption
            )
        else:
            return key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

    @staticmethod
    def load_key(pem_data, is_private=False, password=None):
        """
        Loads a key from PEM format.
        """
        if is_private:
            return serialization.load_pem_private_key(
                pem_data,
                password=password.encode() if password else None,
                backend=default_backend()
            )
        else:
            return serialization.load_pem_public_key(
                pem_data,
                backend=default_backend()
            )

    @staticmethod
    def encrypt_message(message, public_key):
        """
        Encrypts a message using the public key.
        """
        return public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt_message(encrypted_message, private_key):
        """
        Decrypts a message using the private key.
        """
        return private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    @staticmethod
    def generate_symmetric_key():
        """
        Generates a new Fernet key for symmetric encryption.
        """
        return Fernet.generate_key()

    @staticmethod
    def encrypt_with_symmetric_key(message, key):
        """
        Encrypts a message using a Fernet symmetric key.
        """
        f = Fernet(key)
        return f.encrypt(message.encode())

    @staticmethod
    def decrypt_with_symmetric_key(encrypted_message, key):
        """
        Decrypts a message using a Fernet symmetric key.
        """
        f = Fernet(key)
        return f.decrypt(encrypted_message).decode()

# Example usage
if __name__ == "__main__":
    # RSA Encryption Example
    private_key, public_key = CryptoUtils.generate_rsa_keys()
    encrypted_msg = CryptoUtils.encrypt_message("Hello, RSA Encryption!", public_key)
    decrypted_msg = CryptoUtils.decrypt_message(encrypted_msg, private_key)
    print(f"Decrypted RSA message: {decrypted_msg}")

    # Symmetric Encryption Example
    sym_key = CryptoUtils.generate_symmetric_key()
    encrypted_msg = CryptoUtils.encrypt_with_symmetric_key("Hello, Symmetric Encryption!", sym_key)
    decrypted_msg = CryptoUtils.decrypt_with_symmetric_key(encrypted_msg, sym_key)
    print(f"Decrypted symmetric message: {decrypted_msg}")
