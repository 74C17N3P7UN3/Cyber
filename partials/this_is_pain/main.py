from global_utils import base64_decode

with open("ciphertext.txt") as file:
    contents = file.read()

binary_string = (contents
                 .replace("Z", "0")
                 .replace("O", "1"))

base64_string = ""
for byte in binary_string.split():
    base64_string += chr(int(byte, 2))

decoded_bytes = base64_decode(base64_string)
print(decoded_bytes.decode().strip())
