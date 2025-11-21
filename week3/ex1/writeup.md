## Julius Caesar

From the description, decoding `Q2Flc2FyCg==` into `Caesar` suggests the use of a **Caesar Cipher**.

Decoding the **ciphertext** however gives and error, using the usual `b64decode`. This can only mean that the bytes 
themselves were shifted in a `0-255` range, and not just the characters.

We can test all possible shifts using the following code:

```python
ciphertext = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="
decoded_bytes = base64_decode(ciphertext)

for shift in range(256):
    shifted_bytes = bytes((byte + shift) % 256 for byte in decoded_bytes)
```

Since we are only interested in **valid strings** (ASCII contains a lot of non-printable characters), we can prevent 
any errors in the decoding by wrapping it in a `try-catch` block:

```python
try: decoded_string = shifted_bytes.decode("ascii")
except UnicodeDecodeError: continue
```

Finally, since some strings might contain valid characters, but non-representable, we can further reduce the matches 
by wrapping them in an `if` statement:

```python
if decoded_string.isprintable():
    print(decoded_string)
```

This gives us the following output:

```text
Shift 231: dmbqxosBSEz2S^6T^AQT62> |
Shift 232: encryptCTF{3T_7U_BRU73?!}
Shift 233: fodszquDUG|4U`8V`CSV84@"~
```

Obviously, the valid shift is **232**, and the flag ultimately is:

```text
encryptCTF{3T_7U_BRU73?!}
```
