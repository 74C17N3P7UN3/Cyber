from base64 import b32decode, b64decode
from binascii import unhexlify
from string import printable


def b32_decode(message: str):
    message_bytes = message.encode("ascii")
    b32_bytes = b32decode(message_bytes)
    b32_message = b32_bytes.decode("ascii")
    return b32_message


def b64_decode(message: str):
    message_bytes = message.encode("ascii")
    b64_bytes = b64decode(message_bytes)
    b64_message = b64_bytes.decode("ascii")
    return b64_message


def rot_decode(message: str, pos: int):
    alphabet = list(printable)

    rot_dec = ""
    for char in message:
        idx = alphabet.index(char)
        rot_dec += alphabet[(idx - pos) % len(alphabet)]
    return rot_dec


def xor_decode(message: str, key: str = "c4mPar1"):
    rep = len(message) // len(key) + 1
    key = (key * rep)[:len(message)]  # Adjust the key len
    return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(message, key)])


with open("encrypted_flag.txt") as file:
    contents = file.read()

hex_decrypted = unhexlify(contents).decode()
xor_decrypted = xor_decode(hex_decrypted)

msg_decrypted = xor_decrypted
for _ in range(15):
    rot_decrypted = rot_decode(msg_decrypted, 3)
    b32_decrypted = b32_decode(rot_decrypted)
    rot_decrypted = rot_decode(b32_decrypted, 13)
    b64_decrypted = b64_decode(rot_decrypted)
    msg_decrypted = b64_decrypted

print(msg_decrypted)
