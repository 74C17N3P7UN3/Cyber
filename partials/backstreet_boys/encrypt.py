def encryption(plain_text, key):
    encrypted_text = ""
    key_extended = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]

    for i in range(len(plain_text)):
        char_plain = plain_text[i]
        char_key = key_extended[i]

        offset = 97

        if char_plain.isalpha():
            # Here is the most important part
            encrypted_char = chr((ord(char_plain) + ord(char_key) - 2 * offset) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char_plain

    return encrypted_text


flag = "????????????????"
k = "tellmewhy"

c = encryption(flag, k)
print("Encrypted text:", c)  # OUTPUT: ltctfd{p-peye-mp-raee-ieu}
