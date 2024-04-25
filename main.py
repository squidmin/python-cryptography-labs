import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad, pad
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class EncryptRequest(BaseModel):
    plaintext: str


class DecryptRequest(BaseModel):
    ciphertext: str
    iv: str
    key: str


def encrypt_data(plain_text):
    key = get_random_bytes(16)  # AES key length is 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct, base64.b64encode(key).decode('utf-8')


def decrypt_data(ciphertext, iv, key):
    try:
        iv = base64.b64decode(iv)
        key = base64.b64decode(key)
        ct = base64.b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
    except (ValueError, KeyError):
        raise ValueError("Incorrect decryption")


@app.post("/encrypt/")
def encrypt(request: EncryptRequest):
    iv, ciphertext, key = encrypt_data(request.plaintext)
    return {"iv": iv, "ciphertext": ciphertext, "key": key}


@app.post("/decrypt/")
def decrypt(request: DecryptRequest):
    try:
        plaintext = decrypt_data(request.ciphertext, request.iv, request.key)
        return {"plaintext": plaintext}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
