from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os
import secrets
import hashlib
from Crypto.Protocol.KDF import PBKDF2

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to encrypt data
def encrypt(data, password, file):
    salt = secrets.token_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    iv = secrets.token_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    encoded_data = base64.b64encode(salt + iv + encrypted_data).decode('utf-8')
    
    with open(file, "w") as f:
        f.write(encoded_data)

# Function to decrypt data
def decrypt(password, file):
    default_content = {
        "./data/user.txt.enc": "0:0:0:0:0:0\n0",
        "./data/transactions.json.enc": "[]",
        "./data/assets.json.enc": "[]"
    }

    if file in default_content:
        if not os.path.exists(file):
            encrypt(default_content[file], password, file)
            return default_content[file]

    try:
        with open(file, "r") as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        pass

    # Decrypt the data
    decoded_data = base64.b64decode(encrypted_data)
    salt = decoded_data[:16]
    iv = decoded_data[16:32]
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(decoded_data[32:]), AES.block_size).decode('utf-8')
    
    return decrypted_data