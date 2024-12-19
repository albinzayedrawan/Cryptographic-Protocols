# Simulate a Simplified TLS Handshake in Python
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Client generates a random value
client_random = os.urandom(16)

# Server generates a random value and RSA key pair
server_random = os.urandom(16)
server_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
server_public_key = server_private_key.public_key()

# Client encrypts a pre-master secret using the server's public key
pre_master_secret = os.urandom(16)
encrypted_secret = server_public_key.encrypt(
    pre_master_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Server decrypts the pre-master secret
decrypted_secret = server_private_key.decrypt(
    encrypted_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Verify shared secret
assert pre_master_secret == decrypted_secret
print("Shared secret established successfully!")