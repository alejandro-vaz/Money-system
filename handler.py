from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Función para encriptar
def encrypt(data, password, file):
    # Asegúrate de que la longitud de la clave sea de 16, 24 o 32 bytes
    key = (password.encode('utf-8') + b'\0' * 32)[:32]  # Rellenar o truncar la clave
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    transformed = base64.b64encode(encrypted).decode('utf-8')
    with open(file, "w") as file:
        file.write(transformed)


# Función para desencriptar
def decrypt(password, file):
    if file == "./data/user.txt.enc":
        try:
            with open(file, "r") as file:
                encrypted_data = file.read()
        except FileNotFoundError:
            with open(file, "x") as file:
                content = f"""0:0:0:0:0:0
0"""
                encrypt(content, password, "./data/user.txt.enc")
            return content
    if file == "./data/transactions.json.enc":
        try:
            with open(file, "r") as file:
                encrypted_data = file.read()
        except FileNotFoundError:
            with open(file, "x") as file:
                encrypt("[]", password, "./data/transactions.json.enc")
            return "[]"
    if file == "./data/assets.json.enc":
        try:
            with open(file, "r") as file:
                encrypted_data = file.read()
        except FileNotFoundError:
            with open(file, "x") as file:
                encrypt("[]", password, "./data/assets.json.enc")
            return "[]"
    key = (password.encode('utf-8') + b'\0' * 32)[:32]  # Rellenar o truncar la clave
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = base64.b64decode(encrypted_data)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size).decode('utf-8')
    return decrypted