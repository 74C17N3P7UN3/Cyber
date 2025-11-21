## Irreversible encryption

Looking at the `encrypt.py` file, we can tell that we need to **reverse** the process.
I will use **two snippets** for each section, the encryption and the decoding below.

#### Open the file

```python
with open("encrypted_flag.txt", "w") as file:
    file.write(hex_encrypted)
```

```python
with open("encrypted_flag.txt") as file:
    contents = file.read()
```

#### Hex to ASCII

```python
from binascii import hexlify

hex_encrypted = hexlify(message).decode()
```

```python
from binascii import unhexlify

hex_decrypted = unhexlify(contents).decode()
```

#### XOR with the key

```python
xor_encrypted = XORencode(encrypted).encode('ascii')
```

```python
xor_decrypted = xor_decode(hex_decrypted)
```

In this case, the decoding function below is **identical** to the encryption one because of the
XOR property: `A ^ B = C`, but also `C ^ B = A` since we know the **key**.

```python
def xor_decode(message: str, key: str = "c4mPar1"):
    rep = len(message) // len(key) + 1
    key = (key * rep)[:len(message)]  # Adjust the key len
    return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(message, key)])
```

#### Recursive encryption

```python
for _ in range(15):
    b64_encrypted = base64encode(encrypted)
    rot13_encrypted = ROTencode(b64_encrypted, 13)
    b32_encrypted = base32encode(rot13_encrypted)
    encrypted = ROTencode(b32_encrypted, 3)
```

```python
for _ in range(15):
    rot_decrypted = rot_decode(msg_decrypted, 3)
    b32_decrypted = b32_decode(rot_decrypted)
    rot_decrypted = rot_decode(b32_decrypted, 13)
    b64_decrypted = b64_decode(rot_decrypted)
    msg_decrypted = b64_decrypted
```

In order to reverse the process, other than **inverting** the function calls like above, we need to individually check 
the encryption functions involved.

#### Rot cipher

```python
ALPHABET = list(string.printable)
LEN = len(ALPHABET)  # 100

def ROTencode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i+pos)%LEN]
    return rot13_enc
```

```python
def rot_decode(message: str, pos: int):
    alphabet = list(printable)

    rot_dec = ""
    for char in message:
        idx = alphabet.index(char)
        rot_dec += alphabet[(idx - pos) % len(alphabet)]
    return rot_dec
```

This is basically identical, except that we need to **subtract** the otherwise added **key** value.

#### Base32/Base64 decoding

This one is pretty self-explanatory, we just use `base64.b32decode` and `base64.b64decode` instead of their 
corresponding **encoding** functions.

At the end of this (initially tedious) process, we get the flag:

```
spritz{But_wa1t_R3vers1ble_OP3rations_are_B4D}
```