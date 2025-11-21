from global_utils import base64_decode

ciphertext = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="
decoded_bytes = base64_decode(ciphertext)

for shift in range(256):
    shifted_bytes = bytes((byte + shift) % 256 for byte in decoded_bytes)
    try:
        decoded_string = shifted_bytes.decode("ascii")
        if decoded_string.isprintable():
            print(f"Shift {shift}: {decoded_string}")
    except UnicodeDecodeError:
        continue  # Skip invalid shifts that can't be decoded as ASCII
